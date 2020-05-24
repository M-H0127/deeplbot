import asyncio
import collections
import copy
import datetime
import random
import statistics
import time
from time import sleep

import discord

import regex

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzExNDUyMDEwODc2MjM5OTMy.XsDOhQ.hKGHOvuP2DDOnD59ZssB9A2bXDM'
# 接続に必要なオブジェクトを生成
client = discord.Client()

zinroulist=[]
kinsilist=[]
sibarilist=[]
    



@client.event
async def on_message(message):
    global zinroulist

    if client.user != message.author:
        if message.content=="人狼ゲーム":
            channel=message.channel
            if channel in zinroulist:
                await channel.send("既にゲームを始めているよ")
                return
            zinroulist+=[channel]
            me="人狼ルームへようこそ！\nゲームをしたかったら「スタート」って言ってね！（制限時間は60秒)"
            def check(m):
                return m.content=="スタート" and m.channel==channel or channel not in zinroulist
            await channel.send(me)
            try:
                msg=await client.wait_for('message',timeout=60,check=check)
            except asyncio.TimeoutError:
                if channel not in zinroulist:
                    return
                await channel.send("時間切れだよ\nゲームを中断するね")
                zinroulist.remove(channel)
                return
            if channel not in zinroulist:
                return

            m="参加したい人はコメントしてね！\n参加者全員がコメントしたら誰か一人が「募集終了」って言ってね！(制限時間は180秒）"
            def check(m):
                return m.content=="募集終了" and m.channel==channel or channel not in zinroulist
            await channel.send(m)
            a=channel.last_message.created_at
            try:
                msg=await client.wait_for('message',timeout=180,check=check)
            except asyncio.TimeoutError:
                if channel not in zinroulist:
                    return
                await channel.send("時間切れだよ\nゲームを中断するね")
                zinroulist.remove(channel)
                return
            if channel not in zinroulist:
                return
            await channel.send("募集完了")
            b=channel.last_message.created_at
            memberlist=await channel.history(limit=None,before=b,after=a).flatten()
            zinrou={}
            livelist=[]
            deadlist=[]
            for i in memberlist:
                if i.author not in zinrou.keys() and i.author !=client.user:
                    zinrou[i.author]=0
                    livelist+=[i.author]
            
            if channel not in zinroulist:
                return
    
            if len(livelist)<=4:
                m="人数が足りないよ"
                if channel not in zinroulist:
                    return
                await channel.send(m)
                return
            
            elif 5<=len(zinrou)<=6:
                a=random.sample(livelist,4)
                for i in range(4):
                    zinrou[a[i]]=i+1
                for i in livelist:
                    if zinrou[i]==0:
                        zinrou[i]="村人"
                    elif zinrou[i]==1:
                        zinrou[i]="親人狼"
                    elif zinrou[i]==2:
                        zinrou[i]="占い師"
                    elif zinrou[i]==3:
                        zinrou[i]="騎士"
                    elif zinrou[i]==4:
                        zinrou[i]="狂人"
                    dm=await i.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send(zinrou[i])
            elif 7<=len(zinrou)<=8:
                a=random.sample(livelist,5)
                for i in range(5):
                    zinrou[a[i]]=i+1
                for i in livelist:
                    if zinrou[i]==0:
                        zinrou[i]="村人"
                    elif zinrou[i]==1:
                        zinrou[i]="親人狼"
                    elif zinrou[i]==2:
                        zinrou[i]="占い師"
                    elif zinrou[i]==3:
                        zinrou[i]="騎士"
                    elif zinrou[i]==4:
                        zinrou[i]="子人狼"
                    elif zinrou[i]==5:
                        zinrou[i]="霊媒師"
                    dm=await i.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send(zinrou[i])
                
            elif 9<=len(zinrou):
                a=random.sample(livelist,6)
                for i in range(6):
                    zinrou[a[i]]=i+1
                for i in livelist:
                    if zinrou[i]==0:
                        zinrou[i]="村人"
                    elif zinrou[i]==1:
                        zinrou[i]="親人狼"
                    elif zinrou[i]==2:
                        zinrou[i]="占い師"
                    elif zinrou[i]==3:
                        zinrou[i]="騎士"
                    elif zinrou[i]==4:
                        zinrou[i]="子人狼"
                    elif zinrou[i]==5:
                        zinrou[i]="霊媒師"
                    elif zinrou[i]==6:
                        zinrou[i]="狂人"
                    dm=await i.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send(zinrou[i])


            z=[]
            for i in livelist:
                if zinrou[i]=="子人狼" or zinrou[i]=="親人狼":
                    z+=[i]
                if zinrou[i]=="騎士":
                    k=i
                if zinrou[i]=="占い師":
                    u=i
                if zinrou[i]=="霊媒師":
                    r=i
                if zinrou[i]=="狂人":
                    c=i
            syo=""
            for i in z:
                syo+=i.name+"\n"

            for i in z:
                dm=await i.create_dm()
                for q in z:
                    await dm.send(q.name+"さんは"+zinrou[q]+"です\n")
            zin=0
            for i in livelist:
                if zinrou[i]=="子人狼" or zinrou[i]=="親人狼":
                    zin+=1
            dark=zin
            mura=len(livelist)-dark
            me=""
            v=[]
            for i in range(len(livelist)):
                h=str(i+1)
                n=h+":"+livelist[i].name+"\n"
                me+=n
                v+=[h]
            m="DMに役職を送ったよ\n占い師が占うまで待ってね"
            if channel not in zinroulist:
                return
            await channel.send(m)

            dm=await u.create_dm()
            if channel not in zinroulist:
                return
            await dm.send(me)
            if channel not in zinroulist:
                return
            await dm.send("占う人を選んでね\n制限時間は一分")
            def check(m):
                return m.content in v and m.channel==dm or channel not in zinroulist
            try:
                msg=await client.wait_for('message',timeout=60,check=check)
            except asyncio.TimeoutError:
                if channel not in zinroulist:
                    return
                await dm.send("時間切れだよ！")
            else:
                if channel not in zinroulist:
                    return
                people=livelist[int(msg.content)-1]
                role=zinrou[people]
                if role!="子人狼" and role!="親人狼":
                    role="人狼ではない"
                m=people.name+"さんの役職は"+role+"です"
                if channel not in zinroulist:
                    return
                await dm.send(m)
            
            if channel not in zinroulist:
                return
            await channel.send("それでは相談を始めるよ\n3!")
            await asyncio.sleep(1)
            if channel not in zinroulist:
                return
            await channel.send("2!")
            await asyncio.sleep(1)
            if channel not in zinroulist:
                return
            await channel.send("1!")
            await asyncio.sleep(1)

            while zin!=0 and mura>dark:
                guard=-1
                
                me=""
                v=[]
                for i in range(len(livelist)):
                    h=str(i+1)
                    n=h+":"+livelist[i].name+"\n"
                    me+=n
                    v+=[h]
                if channel not in zinroulist:
                    return
                await channel.send("それでは相談を始めてね、相談を終わりたいときは「相談完了」と言ってね")
                def check(m):
                    return m.content=="相談完了" and m.channel==channel or channel not in zinroulist
                try:
                    msg=await client.wait_for('message',timeout=300,check=check)
                except asyncio.TimeoutError:
                    pass
                else:
                    if channel not in zinroulist:
                        return
                
                if channel not in zinroulist:
                    return
                await channel.send("_________________\n相談時間終わり！\n\n人狼だと思う方に投票をしてね\n\n投票方法は今から名簿を送るから\n人狼だと思う人の名前の頭についている数字だけをDMに投稿してね\n投票が可能になったらBOTがDMに呼びかけるのでそれまで待ってね")
                await asyncio.sleep(1)
                if channel not in zinroulist:
                    return
                votemember={}
                for i in livelist:
                    await channel.send("_\n"+i.name+"さんが投票しているよ")
                    dm=await i.create_dm()
                    await dm.send("_________________\n人狼だと思う方に投票をしてね\n\n投票方法は今から名簿を送るから\n人狼だと思う人の名前の頭についている数字だけをDMに投稿してね\n数字は\n「半角」\nで発言してね")
                    await asyncio.sleep(1)
                    if channel not in zinroulist:
                        return
                    await dm.send("_________________\n制限時間は60秒!\n投票しなかった場合、無投票となるのでご注意ください")
                    if channel not in zinroulist:
                        return
                    await dm.send("_\n"+me)
                    await asyncio.sleep(1)
                    if channel not in zinroulist:
                        return
                    await dm.send("_________________\n投票開始")
                    def check(m):
                        return m.content in v and m.channel==dm or channel not in zinroulist
                    try:
                        msg=await client.wait_for('message',timeout=60,check=check)
                    except asyncio.TimeoutError:
                        await dm.send("時間切れだよ")
                    else:
                        if channel not in zinroulist:
                            return
                        votemember[i]=msg.content
                        await dm.send("ありがとう")

                if channel not in zinroulist:
                    return
                await channel.send("終了！！")
                
                if len(votemember)==0:
                    x=[]
                else:
                    x=mode(votemember.values())
                    y=copy.copy(x)
                while len(x)!=1:
                    votemember={}
                    if len(x)==0:
                        if channel not in zinroulist:
                            return
                        await channel.send("_________________\n投票が決まらなかったから、もう一度投票をするよ")
                    else:
                        me=""
                        v=[]
                        we=1
                        for i in x:
                            i=int(i)
                            n=str(we)+":"+livelist[i-1].name+"\n"
                            me+=n
                            v+=[str(we)]
                            we+=1
                        if channel not in zinroulist:
                            return
                        await channel.send("_________________\n投票が決まらなかったから、引き分けなった人でもう一度投票をするよ")
                    await asyncio.sleep(1)
                    if channel not in zinroulist:
                        return
                    await channel.send("_\n"+me)
                    if channel not in zinroulist:
                        return
                    await channel.send("_________________\nやり方はさっきと同じようにDMで行うよ！\nBOT君がDMに来るまで待ってね！")

                    for i in livelist:
                        await channel.send("_\n"+i.name+"さんが投票しているよ")
                        dm=await i.create_dm()
                        await dm.send("_________________\n人狼だと思う方に投票をしてね\n\n投票方法は今から名簿を送るから\n人狼だと思う人の名前の頭についている数字だけをDMに投稿してね\n数字は\n「半角」\nで発言してね")
                        await asyncio.sleep(1)
                        if channel not in zinroulist:
                            return
                        await dm.send("_________________\n制限時間は60秒!\n投票しなかった場合、無投票となるのでご注意ください")
                        if channel not in zinroulist:
                            return
                        await dm.send("_\n"+me)
                        await asyncio.sleep(1)
                        if channel not in zinroulist:
                            return
                        await dm.send("_________________\n投票開始")
                        def check(m):
                            return m.content in v and m.channel==dm or channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=60,check=check)
                        except asyncio.TimeoutError:
                            await dm.send("時間切れだよ")
                        
                        else:
                            if channel not in zinroulist:
                                return
                            votemember[i]=msg.content
                            await dm.send("ありがとう")
                    if channel not in zinroulist:
                        return
                    await channel.send("終了！！")
                    x=mode(votemember.values())
                    for i in range(len(x)):
                        x[i]=y[int(x[i])-1]
                    y=copy.copy(x)

                executer=x[0]
                die=livelist.pop(int(executer)-1)
                deadlist+=[die]
                if channel not in zinroulist:
                    return
                await channel.send("_________________\n"+die.name+"さんが吊るされたよ\n_\n夜になりました")
                zin=0
                for i in livelist:
                    if zinrou[i]=="子人狼" or zinrou[i]=="親人狼":
                        zin+=1
                if zin==0:
                    break
                await asyncio.sleep(1)
                
                if channel not in zinroulist:
                    return
                await channel.send("_________________\n人狼は食べる人を一人\n騎士は守る人を一人選んでね\n今から名簿をDMに送るから\nBOT君にDMで投票と同じ様に名前の前にある数字で教えてね")
                me=""
                v=[]
                for i in range(len(livelist)):
                    n=str(i+1)+":"+livelist[i].name+"\n"
                    me+=n
                    v+=[str(i+1)]
                md=""
                d=[]
                for i in range(len(deadlist)):
                    n=str(i+1)+":"+deadlist[i].name+"\n"
                    md+=n
                    d+=[str(i+1)]
                if k in livelist:
                    dm=await k.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send("人狼が選択するまで待ってね")
                zi=list(set(z)&set(livelist))
                kyou=len(zi)
                if kyou==1:
                    dm=await zi[0].create_dm()
                    if len(z)==2:
                        if channel not in zinroulist:
                            return
                        await dm.send("片方の人狼が死んだことが市民にばれないようにするために、10秒だけ待ってね")
                        def check(m):
                            return channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=10,check=check)
                        except asyncio.TimeoutError:
                            pass
                        else:
                            if channel not in zinroulist:
                                return
                    if channel not in zinroulist:
                        return
                    await dm.send(me)
                    if channel not in zinroulist:
                        return
                    await dm.send("食べる人を教えてね\n60秒以内に選ばれなかったらランダムに選ばれるよ")
                    def check(m):
                        return m.content in v and m.channel==dm or channel not in zinroulist
                    try:
                        msg=await client.wait_for('message',timeout=60,check=check)
                    except asyncio.TimeoutError:
                        eaten=str(random.randrange(len(livelist))+1)
                        if channel not in zinroulist:
                            return
                        await dm.send("時間切れだよ")
                    else:
                        eaten=msg.content
                        if channel not in zinroulist:
                            return
                        await dm.send("ありがとう")
                elif kyou==2:
                    for i in z:
                        if zinrou[i]=="子人狼":
                            z_childe=i
                        elif zinrou[i]=="親人狼":
                            z_adult=i
                    dm=await z_adult.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send("子人狼が選択するまで待ってね")               
                    dm=await z_childe.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send(me)
                    if channel not in zinroulist:
                        return
                    await dm.send("子人狼さん！\n食べる人を教えてね\n60秒以内に選ばれなかったらランダムに選ばれるよ")
                    def check(m):
                        return m.content in v and m.channel==dm or channel not in zinroulist
                    try:
                        msg=await client.wait_for('message',timeout=60,check=check)
                    except asyncio.TimeoutError:
                        eaten=str(random.randrange(len(livelist))+1)
                        if channel not in zinroulist:
                            return
                        await dm.send("時間切れだよ")
                    else:
                        eaten=msg.content
                        if channel not in zinroulist:
                            return
                        await dm.send("ありがとう")
                    dm=await z_adult.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send(me)
                    if channel not in zinroulist:
                        return
                    await dm.send("親人狼さん！\n食べる人を教えてね\n60秒以内に選ばれなかったらランダムに選ばれるよ\n一人目の人狼は"+eaten[0]+"番を選んだよ")
                    def check(m):
                        return m.content in v and m.channel==dm or channel not in zinroulist
                    try:
                        msg=await client.wait_for('message',timeout=60,check=check)
                    except asyncio.TimeoutError:
                        msg.content=0
                        if channel not in zinroulist:
                            return
                        await dm.send("時間切れだよ")
                    else:
                        eaten=msg.content
                        if channel not in zinroulist:
                            return
                        await dm.send("ありがとう")
                if k in livelist:
                    guard=0
                    dm=await k.create_dm()
                    if channel not in zinroulist:
                        return
                    await dm.send(me)
                    if channel not in zinroulist:
                        return
                    await dm.send("守る人を選んでね\n制限時間は60秒！")
                    def check(m):
                        return m.content in v and m.channel==dm or channel not in zinroulist
                    try:
                        msg=await client.wait_for('message',timeout=60,check=check)
                    except asyncio.TimeoutError:
                        guard=-1
                        if channel not in zinroulist:
                            return
                        await dm.send("時間切れだよ")
                    else:
                        if livelist[int(msg.content)-1]!=k:
                            guard=msg.content
                            if channel not in zinroulist:
                                return
                            await dm.send("ありがとう")
                        else:
                            await dm.send("自分自身は選べないよ、もう一度選んでね\n"+me)

                        while guard==0:
                            def check(m):
                                return m.content in v and m.channel==dm or channel not in zinroulist
                            try:
                                msg=await client.wait_for('message',timeout=60,check=check)
                            except asyncio.TimeoutError:
                                guard=-1
                                if channel not in zinroulist:
                                    return
                                await dm.send("時間切れだよ")
                            else:
                                if livelist[int(msg.content)-1]!=k:
                                    guard=msg.content
                                    if channel not in zinroulist:
                                        return
                                    await dm.send("ありがとう")
                                else:
                                    await dm.send("自分自身は選べないよ、もう一度選んでね\n"+me)    

                else:
                    def check(m):
                        return channel not in zinroulist
                    try:
                        msg=await client.wait_for('message',timeout=10,check=check)
                    except asyncio.TimeoutError:
                        pass
                    else:
                        if channel not in zinroulist:
                            return             
                if "霊媒師" in zinrou.values():
                    if channel not in zinroulist:
                        return
                    await channel.send("_________________\n次に占い師は占う人を一人\n霊媒師は占う人を一人選んでね\n今から名簿をDMに送るから\nBOT君にDMで投票と同じ様に名前の前にある数字で教えてね")
                    if r in livelist:
                        dm=await r.create_dm()
                        if channel not in zinroulist:
                            return
                        await dm.send("占い師が選択するまで待ってね")

                    if u in livelist:
                        dm=await u.create_dm()
                        if channel not in zinroulist:
                            return
                        await dm.send(me)
                        if channel not in zinroulist:
                            return
                        await dm.send("占う人を選んでね\n制限時間は一分")
                        def check(m):
                            return m.content in v and m.channel==dm or channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=60,check=check)
                        except asyncio.TimeoutError:
                            if channel not in zinroulist:
                                return
                            await dm.send("時間切れだよ！")
                        else:
                            people=livelist[int(msg.content)-1]
                            role=zinrou[people]
                            if role!="子人狼" and role!="親人狼":
                                role="人狼ではない"
                            m=people.name+"さんの役職は"+role+"です"
                            if channel not in zinroulist:
                                return
                            await dm.send(m)
                    else:
                        def check(m):
                            return channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=10,check=check)
                        except asyncio.TimeoutError:
                            pass
                        else:
                            if channel not in zinroulist:
                                return
                    if r in livelist:
                        dm=await r.create_dm()
                        if channel not in zinroulist:
                            return
                        await dm.send(md)
                        if channel not in zinroulist:
                            return
                        await dm.send("占う人を選んでね\n制限時間は一分")
                        def check(m):
                            return m.content in d and m.channel==dm or channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=60,check=check)
                        except asyncio.TimeoutError:
                            if channel not in zinroulist:
                                return
                            await dm.send("時間切れだよ！")
                        else:
                            people=deadlist[int(msg.content)-1]
                            role=zinrou[people]
                            if role!="子人狼" and role!="親人狼":
                                role="人狼ではない"
                            m=people.name+"さんの役職は"+role+"です"
                            if channel not in zinroulist:
                                return
                            await dm.send(m)
                    else:
                        def check(m):
                            return channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=10,check=check)
                        except asyncio.TimeoutError:
                            pass
                        else:
                            if channel not in zinroulist:
                                return
                else:
                    if channel not in zinroulist:
                        return
                    await channel.send("_________________\n次に占い師は占う人を一人選んでね\n今から名簿をDMに送るから\nBOT君にDMで投票と同じ様に名前の前にある数字で教えてね")
                    if u in livelist:
                        dm=await u.create_dm()
                        if channel not in zinroulist:
                            return
                        await dm.send(me)
                        if channel not in zinroulist:
                            return
                        await dm.send("占う人を選んでね\n制限時間は一分")
                        def check(m):
                            return m.content in v and m.channel==dm or channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=60,check=check)
                        except asyncio.TimeoutError:
                            if channel not in zinroulist:
                                return
                            await dm.send("時間切れだよ！")
                        else:
                            people=livelist[int(msg.content)-1]
                            role=zinrou[people]
                            if role!="子人狼" and role!="親人狼":
                                role="人狼ではない"
                            m=people.name+"さんの役職は"+role+"です"
                            if channel not in zinroulist:
                                return
                            await dm.send(m)
                    else:
                        def check(m):
                            return channel not in zinroulist
                        try:
                            msg=await client.wait_for('message',timeout=10,check=check)
                        except asyncio.TimeoutError:
                            pass
                        else:
                            if channel not in zinroulist:
                                return

                if channel not in zinroulist:
                    return
                await channel.send("_________________\nそれでは朝になりました")

                if guard == eaten:
                    if channel not in zinroulist:
                        return
                    await channel.send("_________________\n騎士が人狼から"+livelist[int(guard)-1].name+"を守りました")
                    
                
                else:
                    die=livelist[int(eaten)-1]
                    deadlist+=[die]
                    livelist.remove(die)
                    if channel not in zinroulist:
                        return
                    await channel.send("_________________\n"+die.name+"さんは食べられました")
                zin=0
                
                guard=-1
                eaten=-2
                for i in livelist:
                    if zinrou[i]=="子人狼" or zinrou[i]=="親人狼":
                        zin+=1

                dark=zin
                mura=len(livelist)-dark
                me=""
                for i in range(len(livelist)):
                    n=str(i+1)+":"+livelist[i].name+"\n"
                    me+=n
                if channel not in zinroulist:
                    return
                await channel.send("_________________\n生存者は\n")
                await asyncio.sleep(1)
                if channel not in zinroulist:
                    return
                await channel.send(me)
            await asyncio.sleep(1)

            muraside=[]
            zinside=[]
            for i in zinrou:
                if zinrou[i]=="子人狼" or zinrou[i]=="親人狼" or zinrou[i]=="狂人":
                    zinside+=[i]
                else:
                    muraside+=[i]
            if zin==0:
                if channel not in zinroulist:
                    return
                await channel.send("_________________\n人狼がいなくなった！\n村人サイドの勝ち\n勝者は")
                for i in muraside:
                    await channel.send(f'{i.mention}さん！')
                    nickname=str(i.nick)
                    if "山田ァ！×" in nickname and "/" in nickname:
                        username=i.name
                        number=[i for i,x in enumerate(nickname) if x=='/']
                        number=number[0]
                        topname=nickname[:number]
                        topname=nickpluss(topname)
                        nickname=topname+'/'+username
                        await i.edit(nick=nickname)
                    else:
                        if i.top_role<message.guild.me.top_role:
                            b=i.name
                            await i.edit(nick="山田ァ！×1/"+b)
            else:
                if channel not in zinroulist:
                    return
                await channel.send("_________________\n人狼サイドの勝ち\n勝者は")
                for i in zinside:
                    await channel.send(f'{i.mention}さん！')
                    nickname=str(i.nick)
                    if "山田ァ！×" in nickname and "/" in nickname:
                        username=i.name
                        number=[i for i,x in enumerate(nickname) if x=='/']
                        number=number[0]
                        topname=nickname[:number]
                        topname=nickpluss(topname)
                        nickname=topname+'/'+username
                        await i.edit(nick=nickname)
                    else:
                        if i.top_role<message.guild.me.top_role:
                            b=i.name
                            await i.edit(nick="山田ァ！×1/"+b)
            zinroulist.remove(channel)

                    
        elif message.content=="人狼リセット":
            if message.channel in zinroulist:
                zinroulist.remove(message.channel)
                await message.channel.send("ゲームを中断したよ")
            else:
                await message.channel.send("ゲームを開始してないよ")

client.run(TOKEN)