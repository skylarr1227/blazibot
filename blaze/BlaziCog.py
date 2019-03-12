from redbot.core import commands
import random
import webbrowser
import sqlite3
##import timer
import discord

class BlaziCog:
    def __init__(self, bot):
        self.bot = bot
        badges=none
        redeems=0
        cash=0
        items=none
    @commands.command(name="start",aliases=['start','begin'])
    async def start(self, ctx,author):
        started=false
        """show pokemon world"""
        """show starters per region"""
        conn = sqlite3.connect('blazidb.db')
        c = conn.cursor()
        c.execute()

        users=c.execute('INSERT INTO Profile('+author+','+badges+','+redeems+','+cash+',' +initiate+','+items+');')
        c.close()

        selectedPokemon=input(self.bot.say("Would out like "+starterfire+" ,"+starterwater+" ,"+" or "+startergrass+"?"))
        randomstatsandNatures(selectedPokemon)
    @commands.command(name="bag",aliases=['bag','backpack','inventory','stuff'])
    async def bag(self, ctx, items: str):
        for item in items:
                await self.bot.say(item)
    @commands.command(name="battle",aliases=['fight','battle'])
    async def battle(self, ctx, pokemonteam: str, Member:str):
        """ battle pokemon"""
        dbsetup('blazidb.db',name,author)
        await acceptBattle(ctx,pokemonteam,discord.Member)
    @commands.command(name="catch_pokemon",aliases=['catch'])
    async def catch_pokemon(self, ctx, pokemon: str):
        """ catch spawned pokemon"""
        dbsetup('blazidb.db',name,author)
        await CPokes(ctx,pokemon)
    @commands.command(name="list_pokes",aliases=['pokemon','p'])
    async def list_pokes(self, ctx, Caughtpokemon: str):
        """ catch spawned pokemon"""
        dbsetup('blazidb.db',name,author)
        await CPokes(ctx,pokemon)
    @commands.command(name="fish",aliases=['fish'])
    async def list_pokes(self, ctx, bag_inventory):
        """check bag for  rod"""
        """fish"""
    @commands.command(name="pokemart",aliases=['mart'])
    async def pokemart(self, ctx, bag_inventory):
        """list pokemart items"""
        """accept user input to buy"""

        dbsetup('blazidb.db',name,author)
    @commands.command(name="buy",aliases=['purchase'])
    async def buy(self, ctx, bank:int):
        """check finances"""
        """see if item exists"""
        """see cost of item"""
        """see if it can be afforded"""
        """minus cost add item to  inventory"""
        dbsetup('blazidb.db',name,author)
    @commands.command(name="profile",aliases=['profile','bal','balance','me'])
    async def profile(self, ctx):
        """check profile from db"""
        """print name badges currency and redeems"""
        dbsetup('blazidb.db',name,author)
    @commands.command(name="donate",aliases=['donate'])
    async def donate(self, ctx):
        webbrowser.open('http://ko-fi.com/blazibot')
        """checkrole"""
        """sliding scale"""
    @commands.command(name="filter",aliases=['f'])
    async def filter(self, ctx, filtercmd:str):
        """check if filtercmd contains pokemon or market"""
        """check if filtercmd contains type or name"""
    @commands.command(name="breed",aliases=['b'])
    async def breed(self, ctx, pokemale:str,pokefemale):
        conn = sqlite3.connect('blazidb.db')
        c = conn.cursor()
        pokemalegroup=c.execute("SELECT egggroups1 AND egggroups2 FROM poke WHERE pokemale==identifier")
        pokeefemgroup=c.execute("SELECT egggroups1 AND egggroups2 FROM poke WHERE pokefemale==identifier")
        list(pokemalegroup)
        list(pokeefemgroup)
        if(pokemalegroup==pokeefemgroup):
                pokemalegend=c.execute("SELECT gender_rate FROM OwnedPokes WHERE numbercaught=="+pokemale)
                pokefemgend=c.execute("SELECT gender_rate FROM OwnedPokes WHERE numbercaught=="+pokefemale)
                list(pokemalegend)
                list(pokemafemgend)
                if(pokegend!=pokeefemgend or pokemale=='ditto'or pokefemale=='ditto'):
                        malestats=c.execute("SELECT hp AND atk  AND  def AND  speed AND spatk AND spdef FROM OwnedPokes WHERE numbercaught==pokemale").fetchall()
                        femalestats=c.execute("SELECT hp AND atk  AND  def AND  speed AND spatk AND spdef FROM OwnedPokes WHERE numbercaught==pokefemale").fetchall()
                        a=randint(1,6)
                        b=randint(1,6)
                        c=randint(1,6)
                        x=randint(1,6)
                        y=randint(1,6)
                        z=randint(1,6)
                        babypoke=none
                        babypoke[a]=malestats[a]
                        babypoke[b]=malestats[b]
                        babypoke[c]=malestats[c]
                        babypoke[x]=femalestats[x]
                        babypoke[y]=femalestats[y]
                        babypoke[z]=femalestats[z]
                        i=1
                        while(babypoke.contains('0') and i<7):
                                for stat in babypoke[i]:
                                    if(stat[i]!=babypoke[a] or stat[i]!=babypoke[b] or stat[i]!=babypoke[c] or stat[i]!=babypoke[x] or stat[i]!=babypoke[y] or stat[i]!=babypoke[z]):
                                        newstat=randint(0,31)
                                        babypoke[i]=newstat
                                        i=i+1

                                        continue
                            #add babypoke to sql
                        else:
                            bot.say("You cannot breed two of the same gender!")

        else:
                bot.say("These two Pokemon are not compatible!")
        """check egg groups"""
        """check gender"""
        """create egg"""
        """create new poke"""
        """call randomstatsandnatures"""
    @commands.command(name="buy",aliases=['b'])
    async def buy(self, ctx,item:str):
        @commands.command(name="set",aliases=['set'])
        async def set(self, ctx,selectedPokemon):
            conn = sqlite3.connect('blazidb.db')
            c = conn.cursor()
##            poketype=c.execute("SELECT type FROM Poke WHERE "+selectedPokemon="Identifier")
            setsposs=c.execute("SELECT identifier FROM type_id="+poketype)
            set=list(setsposs)
            bot.say(set)
        @commands.command(name="moves",aliases=['moves'])
        async def moves(self, ctx,selectedPokemon):
            conn = sqlite3.connect('blazidb.db')
            c = conn.cursor()
            mov=c.execute("SELECT move1 AND move2 AND move3 AND move4 from OwnedPokes")
            bot.say(list(mov))
        @commands.command(name="info",aliases=['i'])
        async def info(self, ctx,pokenum:int):
            """seleced poke"""
            """display pic ivs and evs and exp"""
            conn = sqlite3.connect('blazidb.db')
            c = conn.cursor()
            pokeinfo=c.execute("SELECT * FROM OwnedPokes WHERE numb==pokenum").fetchall()
            for infor in pokeinfo:
                    bot.say(infor)

            @commands.command(name="party",aliases=['party','favs','team'])
            async def party(self, ctx,poketeam:str):
                conn = sqlite3.connect('blazidb.db')
                c = conn.cursor()
                part=c.execute("SELECT poke FROM Party WHERE id=="+author)
                ty=list(part)
                bot.say(ty)


        def leveling(author,selectedPokemon):
            def maxexp(author,selectedPokemon):
                lv=selectedPokemon.level
        if(lv<51):
                experienceneeded=lv*lv*lv
                experienceneeded=experienceneeded*(100-lv)
                experienceneeded=experienceneeded/50
        elif(lv<=100 and lv>50):
                experienceneeded=lv*lv*lv
                experienceneeded=experienceneeded*(150-lv)
                experienceneeded=experienceneeded/100

        def expgain(author,selectedPokemon,gained:int):
                """gain exp from message or battle"""
                if(expe>=experienceneeded):
                        selectedPokemon.level=level+1
                        expe=expe-experienceneeded
                        evolution(author,selectedPokemon)
    def evolution(author,selectedPokemon):
        notregevolve='false'
        Tradeevo=["kadabra","haunter","boldore","machoke","graveler","pumpkaboo","phantump","poliwhirl(kings rock)","slowpoke(kings rock)","Onix(metal coat)","scyther(metal coat)","seadra(dragon scale)","porygon(up-grade)","dusclops(reaper cloth)","clamperl(deep sea scale,deep sea tooth)","rhydon(protector)","electabuzz(electrizer)","Magmar(magmarizer)","porygon2(dubious disk)","swirlix(whipped dream)","spritzee(satchet)"]
        Moonstoneevo=["nidorino","nidorina","clefairy","jigglypuff","skitty","munna"]
        Happinessevo=["Pichu","munchlax","Golbat","togepi","chansey","buneary"]
        Dayevo=["Eevee(happiness)","Riolu(hapiness)","budew(hapiness)","happiny(oval stone)","tyrunt"]
        Nightevo=["Eevee(happiness)","chingling(happiness)","gligar(razor fang)","sneasle(razor claw)","amaura"]
        Moveevo=["mime jr.(mimic)","aipom(double hit)","tangela(ancient power)","bonsly(mimic)","lickitung(rollout)","yanma(ancient power)"]
        Waterstoneevo=["eevee","poliwhirl","shellder","staryu","lombre"]
        Sunstoneevo=["sunkern","gloom"]
        Firestoneevo=["vulpix","growlithe","eevee"]
        Icestoneevo=["eevee","alolan-vulpix","alolan-sandshrew"]
        Thunderstoneevo=["pikachu","eevee"]
        Shinystoneevo=["roselia","togetic"]
        Dawnstoneevo=["kirlia","snorunt"]
        Dawnstoneevo["misdreavus","murkrow"]
        if(Tradeevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Moonstoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Happinessevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Dayevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(NighMoveevotevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Moveevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Waterstoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Sunstoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Firestoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Icestoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Thunderstoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Shinystoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Dawnstoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Thunderstoneevo.contains(selectedPokemon)):
                notregevolve='true'
        elif(Dawnstoneevo.contains(selectedPokemon)):
                notregevolve='true'
        else:
                notregevolve='false'
        if selectedPokemon=='Eevee':
                notregevolve='false'

    def CPokes(ctx,pokemon,message):
        caught=false
        run_away=false
        t=timer(3600,ifcaught)
        while  t>0:
                if run_away==false:
                        run=rand.randint(0,8)
                        if run==0:
                                run_away=true
                                break
                        else:
                                if message.contains('catch'):
                                        msg=message.split
                                        conn = sqlite3.connect('blazidb.db')
                                        c = conn.cursor()
                                        pokename=c.execute("SELECT Identifier FROM Pokes WHERE numb==pokemon").fetchall()
                                        c.close()
                                        if pokename==msg[2]:
                                                caught=true
                                                randomstatsandNatures(pokemon)
                                                conn = sqlite3.connect('blazidb.db')

                                                break
                                        else:
                                                caught=false
    def Spawn(Pokes):
        spawned=rand.randint(1,807)
        conn = sqlite3.connect('blazidb.db')
        c = conn.cursor()
        spn=c.execute("SELECT `Img AND Identifier FROM poke WHERE numb==spawned").fetchall()

        conn.close()
        bot.say("A Wild Pokemon Appeared!")
        CPokes(ctx,spn[1])
    def ifcaught():
        run_away=true
##    #def acceptBattle(ctx,discord.author.selectedPokemon,discord.Member.selectedPokemon)
##        battleacc=input(bot.say(discord.Member +" "+ author +" has challenged you to a battle! Do you accept?"))
##        conn = sqlite3.connect('blazidb.db')
##        c = conn.cursor()
##        part=c.execute("SELECT poke FROM Party WHERE id=="+author)
##        pokemonteam1=part
##        part2=c.execute("SELECT poke FROM Party WHERE id=="+discord.Member)
##        pokemon2team=part2
##        if(battleacc=='yes'or'y' or 'yeah'):
##                poke1=author.selectedPokemon
##                poke2=discord.Member.selectedPokemon
##                BattlePokes(ctx,poke1,poke2,discord.Member,author)
##                """BattlePokes(ctx,pokemonteam1,discord.Member,author,pokemonteam2)"""
##        else:
##                break
##    #def BattlePokes(ctx,poke1,poke2,discord.Member,author):
##        """show pokes"""
##        bot.say(poke1.name+" vs "+poke2.name)
##        """FOR LOOP GETTING STATS OF pokes"""
##        while(poke1.hp >0 or poke2.hp>0):
##                if(poke1.speed>poke2.speed):
##                        spdone='higher'
##                        atk1=input(bot.say(author+"choose your attack"))
##                else:
##                        spdtwo='higher'
##                        atk2=input(bot.say(author+"choose your attack"))
##                if(atk1!=null and spdone=='higher'):
##                        """get move stat  vs    base dmg and minus hp"""
##                        if(statmoves.contains(atk1)):
##                                """do stat effect"""
##                elif(atk2!=null and spdone=='higher'):
##                        """get move stat  vs    base dmg and minus hp"""
##                        if(statmoves.contains(atk2)):
##                                """do stat effect"""
##        if(poke1.hp>=0):
##                gained=(poke1.level-(poke2.level/10)*10)
##                expgain(author,poke2,gained)
##        elif(poke2.hp>=0):
##                gained=(poke2.level-(poke1.level/10)*10)
##                expgain(author,poke1,gained)
##    def dbsetup(dbname: str,name,author):
##        conn = sqlite3.connect('blazidb.db')
##        c = conn.cursor()
##        if(name=="profile" or name=="pokemon" or name=="p"or name.contains("f") or name.contains("filter")):
##                #open user info
##                me=c.execute("SELECT * FROM Profile WHERE name = '%s'" %author)
##                list(me)
##                for mystuff in me:
##                        bot.say(mystuff)
##        elif(name=="market"or name=="m"):
##            conn = sqlite3.connect('blazidb.db')
##            c = conn.cursor()
##            c.execute()
##
##            marketlist=c.execute('SELECT identifier FROM Market').fetchall()
##        for stuffm in marketlist:
##                bot.say(stuffm)
##
##        #selectedPokemon=input(self.bot.say("Would out like "+starterfire+" ,"+starterwater+" ,"+" or "+startergrass"))
##        randomstatsandNatures(selectedPokemon
##                #market=c.execute("SELECT * FROM market").fetchall()
##                #for item in market:
##                        (bot.say(item)
##        #elif(name=="shop" or name=="pokemart"):
##                #shopstuff=c.execute("SELECT * FROM OwnedPokes WHERE name = '%s'" %author).fetchall()
##               # for stuffs in shopstuff:
##                       # bot.say(stuffs)
##        #elif(name="Spawn"):
##                #rand from pokemon list
##        #else:
##               #break
##        #conn.close()
    def randomstatsandNatures(selectedPokemon):
        NewHPIV=rand.randint(0,31)
        NewATKIV=rand.randint(0,31)
        NewDEFIV=rand.randint(0,31)
        NewSPATKIV=rand.randint(0,31)
        NewSPDEFIV=rand.randint(0,31)
        NewSPEEDIV=rand.randint(0,31)

        #put rand ability
        randnat=rand.randint(0,24)
        conn = sqlite3.connect('blazidb.db')
        c = conn.cursor()
        nat=c.execute("SELECT * FROM Natures").fetchall()
        nature=nat[randnat]
        conn = sqlite3.connect('blazidb.db')
        c = conn.cursor()
        gend=c.execute("SELECT gender_rate FROM poke WHERE identifier==selectedPokemon AND COL").fetchall()
        conn.close()
        if(gend==0):
                pokegend='male'
        elif(gend==1):
                x=rand.randint(0,7)
                if(x==0):
                        pokegend='female'
                else:
                        pokegend='male'
        elif(gend==2):
                x=rand.randint(0,4)
                if(x==0):
                        pokegend='female'
                else:
                        pokegend='male'
        elif(gend==4):
                x=rand.randint(0,1)
                if(x==0):
                        pokegend='female'
                else:
                        pokegend='male'
        elif(gend==6):
                x=rand.randint(0,4)
                if(x==0):
                        pokegend='male'
                else:
                        pokegend='female'
        elif(gend==7):
                x=rand.randint(0,7)
                if(x==0):
                        pokegend='male'
                else:
                        pokegend='female'
        elif(gend==8):
                pokegend=='female'
##        else:
##                pokegend='genderless'
##        TotalIV=((NewSPEEDIV+NewSPDEFIV+NewSPATKIV+NewDEFIV+NewATKIV+NewHPIV)/1.86)
##        selectedPokemon(nature,NewHPIV,NewATKIV,NewDEFIV,NewSPATKIV,NewSPDEFIV,NewSPEEDIV,TotalIV)
##        conn = sqlite3.connect('blazidb.db')
##        c = conn.cursor()
##       rows=c.execute('SELECT Count(*) FROM OwnedPokes')
##        pokenumber=c.execute('SELECT numb FROM Pokes WHERE Identifier='selectedPokemon)
##        c.execute('INSERT INTO OwnedPokes('pokenumber','rows+1','level','NewATKIV','NewDEFIV','NewSPATKIV','NewSPDEFIV','NewSPEEDIV',0,0'');')



