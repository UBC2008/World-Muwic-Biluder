
#MP3文件转midi文件
def Mp32Mid(mp3File, midFile):
    from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
    # 加载
    (audio, _) = load_audio(mp3File, sr=sample_rate, mono=True)
    # 实例化并转换
    PianoTranscription(device="cpu").transcribe(audio, midFile)



#传入一个音符列表转为指令列表
def Note2Cmd(Notes : list,EntityName:str,ScoreboardName:str,Instrument:str, PlayerSelect:str='') -> list:
    commands = []
    a = 0.0
    for i in range(len(Notes)):
        commands.append("execute @e[name=\""+EntityName+"\",scores={"+ScoreboardName+"="+str(int((a+2)*5+int(Notes[i][1]*5)))+"}] ~ ~ ~ execute @a"+PlayerSelect+" ~ ~ ~ playsound "+Instrument+" @s ~ ~ ~ 1000 "+str(Notes[i][0])+" 1000\n")
        a += Notes[i][1]
    commands.append("\n\n# 凌云我的世界开发团队 x 凌云软件开发团队  : W-YI（金羿）\n")
    return commands








import amulet
import amulet_nbt
from amulet.api.block import Block
from amulet.api.block_entity import BlockEntity
from amulet.utils.world_utils import block_coords_to_chunk_coords
from amulet_nbt import TAG_String,TAG_Compound



#简单载入方块
#level.set_version_block(posx,posy,posz,"minecraft:overworld",("bedrock", (1, 16, 20)),Block(namespace, name))



#转入指令列表与位置信息转至世界
def Cmd2World(cmd:list,world:str,dire:list):
    level = amulet.load_level(world)
    cdl = []
    for i in cmd:
        if (i[:i.index('#')].replace(' ','') != '\n') and(i[:i.index('#')].replace(' ','') != ''):
            cdl.append(i[:i.index('#')].replace(' ',''))
    i = 0
    for j in cdl:
        if dire[1]+i >= 255:
            dire[0]+=1
            i=0
        #定义此方块
        if i == 0:
            universal_block = Block('universal_minecraft','command_block',{'conditional':TAG_String("false"),'facing':TAG_String('up'),'mode':TAG_String("repeating")})
        else:
            universal_block = Block('universal_minecraft','command_block',{'conditional':TAG_String("false"),'facing':TAG_String('up'),'mode':TAG_String("chain")})
        #定义方块实体
        universal_block_entity = BlockEntity( 'universal_minecraft','command_block',dire[0],dire[1]+i,dire[2],amulet_nbt.NBTFile(TAG_Compound({'utags': TAG_Compound({'Command': TAG_String(j)}) })))
        cx, cz = block_coords_to_chunk_coords(dire[0], dire[2])
        #获取区块
        chunk = level.get_chunk(cx, cz, "minecraft:overworld")
        offset_x, offset_z = dire[0] - 16 * cx, dire[2] - 16 * cz
        #将方块加入世界
        chunk.blocks[offset_x, dire[1]+i, offset_z] = level.block_palette.get_add_block(universal_block)
        chunk.block_entities[(dire[0], dire[1]+i, dire[2])] = universal_block_entity
        #设置为已更新区块
        chunk.changed = True
        #保存世界
        level.save()
        i+=1
    del i, cdl
    level.close()


#放置普通方块
def Block2World(world:str,dire:list,blockname:str):
    level = amulet.load_level(world)
    level.set_version_block(dire[0],dire[1],dire[2],"minecraft:overworld",("bedrock", (1, 16, 20)),Block("minecraft", blockname))
    level.save()


#加载一堆世界方块到世界里头
def Blocks2World(world:str,dire:list,Datas:list):
    from nmcsup.const import Blocks
    i = 0
    for j in Datas:
        if dire[1]+1 >= 255:
            i = 0
            dire[0]+=1
        Block2World(world,[dire[0],dire[1]+i,dire[2]],Blocks[j[0]])
        i = int(i+j[1]+0.5)    #四舍五入


def Note2Player(dire:list,Notes:list,CmdData:list) -> list:
    from nmcsup.const import Blocks
    Cmds = []
    for j in Notes:
        Cmds.append('execute @e[y='+str(dire[1])+',dy='+str(255-dire[1])+',name='+CmdData['Ent']+'] ~ ~ ~ detect ~ ~ ~ '+Blocks[j]+' 0 execute @a '+CmdData['Pls']+' ~ ~ ~ playsound '+CmdData['Ins']+' @s ~ ~ ~ 1000 '+str(j)+' 1000\n')
    Cmds+=['#世界音创开发\n','execute @e[y='+str(dire[1])+',dy='+str(255-dire[1])+',name='+CmdData['Ent']+'] ~ ~ ~ tp ~ ~1 ~\n','execute @e[y=255,dy=100,name='+CmdData['Ent']+'] ~ ~ ~ tp ~1 '+str(dire[1])+' ~\n']
    return Cmds



#传入音符列表制作播放器指令
def Notes2Player(NoteData,world:str,dire:list,CmdData:dict):
    Notes = {}
    for i in NoteData:
        for j in i:
            Notes[j[0]] = ''
    Notes = list(Notes.keys())
    Cmds = Note2Player(dire,Notes,CmdData)
    return Cmds








#传入音符列表生成方块至世界
def Datas2BlkWorld(NoteData,world:str,dire:list):
    for i in range(len(NoteData)):
        Blocks2World(world,[dire[0],dire[1],dire[2]+i],NoteData[i])



#传入音符列表生成指令至世界
def Datas2CmdWorld(NoteData,world:str,dire:list,CmdData:dict):
    for i in range(len(NoteData)):
        Cmd2World(Note2Cmd(NoteData[i],CmdData['Ent'],CmdData['Sbn'],CmdData['Ins'],CmdData['Pls']),world,[dire[0],dire[1],dire[2]+i])





