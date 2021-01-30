import pygame, sys, time, remix_char

from pygame.locals import *




def opcion_1():
    
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 10)
    myfont_stocks = pygame.font.SysFont("Comic Sans MS", 27)
    cont_texto = 48
    cont_texto2 = 48
    texto2 = "Designed by Nax & Bob"
    texto3 = "48"
    texto_2 = myfont.render(texto2,False,(255,255,255))
    texto_3 = myfont_stocks.render(texto3,False,(255,255,255))
    texto_4 = myfont_stocks.render(texto3,False,(255,255,255))
    

    # Texto
    textoCK = False
    texto2CK = False
    
    
    
    
    # Creación de la ventana

    pygame.init()
    ventana = pygame.display.set_mode((800,645))
    pygame.display.set_caption("12 Character Battle Chart  V 2.0")
    pygame.display.set_icon(pygame.image.load("images/smash_ico.png"))

    # Creacion de las imagenes -----------------------------------------------
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    # Fila 1

    # Luigi
    stock_luigi_1 = pygame.image.load("images/stock_luigi.jpg")
    stock_luigi_1 = pygame.transform.scale(stock_luigi_1, (15,15))
    stock_luigi_1_CK = True
    stock_luigi_2_CK = True
    stock_luigi_3_CK = True
    stock_luigi_4_CK = True
    contador_luigi = 4
    luigi = pygame.image.load("images/luigi.jpg")
    luigi = pygame.transform.scale(luigi, (100, 100))
    luigid = pygame.image.load("images/luigid.jpg")
    luigid = pygame.transform.scale(luigid, (100,100))
    luigiCK = True

    # Mario
    stock_mario_1 = pygame.image.load("images/stock_luigi.jpg")
    stock_mario_1 = pygame.transform.scale(stock_mario_1, (15,15))
    stock_mario_1_CK = True
    stock_mario_2_CK = True
    stock_mario_3_CK = True
    stock_mario_4_CK = True
    contador_mario = 4
    mario = pygame.image.load("images/mario.jpg")
    mario = pygame.transform.scale(mario, (100, 100))
    mariod = pygame.image.load("images/mariod.jpg")
    mariod = pygame.transform.scale(mariod, (100,100))
    marioCK = True

    # DK
    stock_dk_1 = pygame.image.load("images/banana.jpg")
    stock_dk_1 = pygame.transform.scale(stock_dk_1, (22,22))
    stock_dk_1_CK = True
    stock_dk_2_CK = True
    stock_dk_3_CK = True
    stock_dk_4_CK = True
    contador_dk = 4
    dk = pygame.image.load("images/dk.jpg")
    dk = pygame.transform.scale(dk, (100,100))
    dkd = pygame.image.load("images/dkd.jpg")
    dkd = pygame.transform.scale(dkd, (100,100))
    dkCK = True

    # Link
    stock_link_1 = pygame.image.load("images/heartrojo.png")
    stock_link_1 = pygame.transform.scale(stock_link_1, (30,30))
    stock_link_2 = pygame.image.load("images/heartrojo.png")
    stock_link_2 = pygame.transform.scale(stock_link_2, (30,30))
    stock_link_3 = pygame.image.load("images/heartrojo.png")
    stock_link_3 = pygame.transform.scale(stock_link_3, (30,30))
    stock_link_4 = pygame.image.load("images/heartrojo.png")
    stock_link_4 = pygame.transform.scale(stock_link_4, (30,30))
    stock_link_55 = pygame.image.load("images/heartnegro.png")
    stock_link_55 = pygame.transform.scale(stock_link_55, (30,30))
    stock_link_66 = pygame.image.load("images/heartnegro.png")
    stock_link_66 = pygame.transform.scale(stock_link_66, (30,30))
    stock_link_77 = pygame.image.load("images/heartnegro.png")
    stock_link_77 = pygame.transform.scale(stock_link_77, (30,30))
    stock_link_88 = pygame.image.load("images/heartnegro.png")
    stock_link_88 = pygame.transform.scale(stock_link_88, (30,30))
    life_past = pygame.image.load("images/lifepast.png")
    life_past = pygame.transform.scale(life_past, (60,60))
    stock_link_1_CK = True
    stock_link_2_CK = True
    stock_link_3_CK = True
    stock_link_4_CK = True
    life_pastCK = True
    contador_link = 4
    link = pygame.image.load("images/link.jpg")
    link = pygame.transform.scale(link, (100,100))
    linkd = pygame.image.load("images/linkd.jpg")
    linkd = pygame.transform.scale(linkd, (100,100))
    linkCK = True

    # Samus
    energy = pygame.image.load("images/energy0.png")
    energy = pygame.transform.scale(energy, (40,10))
    stock_samus_1 = pygame.image.load("images/pink.png")
    stock_samus_1 = pygame.transform.scale(stock_samus_1, (15,15))
    stock_samus_5 = pygame.image.load("images/brown.png")
    stock_samus_5 = pygame.transform.scale(stock_samus_5, (15,15))
    stock_samus_1_CK = True
    stock_samus_2_CK = True
    stock_samus_3_CK = True
    stock_samus_4_CK = True
    energyCK = True
    contador_samus = 4
    samus = pygame.image.load("images/samus.jpg")
    samus = pygame.transform.scale(samus, (100,100))
    samusd = pygame.image.load("images/samusd.jpg")
    samusd = pygame.transform.scale(samusd, (100,100))
    samusCK = True

    # C. Falcon
    stock_falcon_0 = pygame.image.load("images/fz_energy1.png")
    stock_falcon_0 = pygame.transform.scale(stock_falcon_0, (90,25))
    stock_falcon_1 = pygame.image.load("images/fz_energy2.png")
    stock_falcon_1 = pygame.transform.scale(stock_falcon_1, (85,20))
    bar1 = pygame.image.load("images/bar1.png")
    bar1 = pygame.transform.scale(bar1, (56,2))
    bar2 = pygame.image.load("images/bar2.png")
    bar2 = pygame.transform.scale(bar2, (2,16))
    bar22CK = True
    bar22CK_2 = True
    bar1CK = True
    bar2CK = True
    stock_falcon_0_CK = True
    stock_falcon_1_CK = True
    stock_falcon_2_CK = True
    stock_falcon_3_CK = True
    stock_falcon_4_CK = True
    contador_falcon = 4
    falcon = pygame.image.load("images/falcon2.jpg")
    falcon = pygame.transform.scale(falcon, (100,100))
    falcond = pygame.image.load("images/falcond.jpg")
    falcond = pygame.transform.scale(falcond, (100,100))
    falconCK = True

    # Ness
    stock_ness_1 = pygame.image.load("images/hp.png")
    stock_ness_1 = pygame.transform.scale(stock_ness_1, (19,17))
    stock_ness_2 = pygame.image.load("images/cero.png")
    stock_ness_2 = pygame.transform.scale(stock_ness_2, (17,17))
    stock_ness_3 = pygame.image.load("images/cero.png")
    stock_ness_3 = pygame.transform.scale(stock_ness_3, (17,17))
    stock_ness_4 = pygame.image.load("images/cero.png")
    stock_ness_4 = pygame.transform.scale(stock_ness_4, (17,17))
    stock_ness_5 = pygame.image.load("images/uno.png")
    stock_ness_5 = pygame.transform.scale(stock_ness_5, (17,17))
    stock_ness_6 = pygame.image.load("images/dos.png")
    stock_ness_6 = pygame.transform.scale(stock_ness_6, (17,17))
    stock_ness_7 = pygame.image.load("images/tres.png")
    stock_ness_7 = pygame.transform.scale(stock_ness_7, (17,17))
    stock_ness_8 = pygame.image.load("images/cuatro.png")
    stock_ness_8 = pygame.transform.scale(stock_ness_8, (17,17))
    stock_ness_1_CK = True
    stock_ness_2_CK = True
    stock_ness_3_CK = True
    stock_ness_4_CK = True
    stock_ness_5_CK = False
    stock_ness_6_CK = False
    stock_ness_7_CK = False
    stock_ness_8_CK = True
    contador_ness = 4
    ness = pygame.image.load("images/ness.jpg")
    ness = pygame.transform.scale(ness, (100,100))
    nessd = pygame.image.load("images/nessd.jpg")
    nessd = pygame.transform.scale(nessd, (100,100))
    nessCK = True

    # Yoshi
    stock_yoshi_1 = pygame.image.load("images/egg.jpg")
    stock_yoshi_1 = pygame.transform.scale(stock_yoshi_1, (18,18))
    stock_yoshi_1_CK = True
    stock_yoshi_2_CK = True
    stock_yoshi_3_CK = True
    stock_yoshi_4_CK = True
    contador_yoshi = 4
    yoshi = pygame.image.load("images/yoshi.jpg")
    yoshi = pygame.transform.scale(yoshi, (100,100))
    yoshid = pygame.image.load("images/yoshid.jpg")
    yoshid = pygame.transform.scale(yoshid, (100,100))
    yoshiCK = True

    # Kirby
    stock_kirby_1 = pygame.image.load("images/tomato.png")
    stock_kirby_1 = pygame.transform.scale(stock_kirby_1, (30,30))
    stock_kirby_1_CK = True
    stock_kirby_2_CK = True
    stock_kirby_3_CK = True
    stock_kirby_4_CK = True
    contador_kirby = 4
    kirby = pygame.image.load("images/kirby.jpg")
    kirby = pygame.transform.scale(kirby, (100,100))
    kirbyd = pygame.image.load("images/kirbyd.jpg")
    kirbyd = pygame.transform.scale(kirbyd, (100,100))
    kirbyCK = True

    # Fox
    stock_fox_1 = pygame.image.load("images/ship.jpg")
    stock_fox_1 = pygame.transform.scale(stock_fox_1, (18,18))
    stock_fox_1_CK = True
    stock_fox_2_CK = True
    stock_fox_3_CK = True
    stock_fox_4_CK = True
    contador_fox = 4
    fox = pygame.image.load("images/fox.jpg")
    fox = pygame.transform.scale(fox, (100,100))
    foxd = pygame.image.load("images/foxd.jpg")
    foxd = pygame.transform.scale(foxd, (100,100))
    foxCK = True

    # Pikachu
    stock_pikachu_1 = pygame.image.load("images/pokeball.jpg")
    stock_pikachu_1 = pygame.transform.scale(stock_pikachu_1, (19,19))
    stock_pikachu_1_CK = True
    stock_pikachu_2_CK = True
    stock_pikachu_3_CK = True
    stock_pikachu_4_CK = True
    contador_pikachu = 5
    pikachu = pygame.image.load("images/pikachu.jpg")
    pikachu = pygame.transform.scale(pikachu, (100,100))
    pikachud = pygame.image.load("images/pikachud.jpg")
    pikachud = pygame.transform.scale(pikachud, (100,100))
    pikachuCK = True


    # Jigglypuff
    stock_jigglypuff_1 = pygame.image.load("images/pokeball.jpg")
    stock_jigglypuff_1 = pygame.transform.scale(stock_jigglypuff_1, (19,19))
    stock_jigglypuff_1_CK = True
    stock_jigglypuff_2_CK = True
    stock_jigglypuff_3_CK = True
    stock_jigglypuff_4_CK = True
    contador_jigglypuff = 4
    jigglypuff = pygame.image.load("images/jigglypuff.jpg")
    jigglypuff = pygame.transform.scale(jigglypuff, (100,100))
    jigglypuffd = pygame.image.load("images/jigglypuffd.jpg")
    jigglypuffd = pygame.transform.scale(jigglypuffd, (100,100))
    jigglypuffCK = True


    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Fila 2

    # Luigi
    stock_luigi_1_CK_2 = True
    stock_luigi_2_CK_2 = True
    stock_luigi_3_CK_2 = True
    stock_luigi_4_CK_2 = True
    contador_luigi_2 = 4
    luigi1 = pygame.image.load("images/luigi.jpg")
    luigi1 = pygame.transform.scale(luigi1, (100, 100))
    luigid1 = pygame.image.load("images/luigid.jpg")
    luigid1 = pygame.transform.scale(luigid1, (100,100))
    luigiCK1 = True

    # Mario
    stock_mario_1_CK_2 = True
    stock_mario_2_CK_2 = True
    stock_mario_3_CK_2 = True
    stock_mario_4_CK_2 = True
    contador_mario_2 = 4
    
    marioCK = True
    
    marioCK1 = True

    # DK
    stock_dk_1_2 = pygame.image.load("images/banana.jpg")
    stock_dk_1_2 = pygame.transform.scale(stock_dk_1, (22,22))
    stock_dk_2_2 = pygame.image.load("images/banana.jpg")
    stock_dk_2_2 = pygame.transform.scale(stock_dk_2_2, (22,22))
    stock_dk_3_2 = pygame.image.load("images/banana.jpg")
    stock_dk_3_2 = pygame.transform.scale(stock_dk_3_2, (22,22))
    stock_dk_4_2 = pygame.image.load("images/banana.jpg")
    stock_dk_4_2 = pygame.transform.scale(stock_dk_4_2, (22,22))
    stock_dk_1_CK_2 = True
    stock_dk_2_CK_2 = True
    stock_dk_3_CK_2 = True
    stock_dk_4_CK_2 = True
    contador_dk_2 = 4
    dk1 = pygame.image.load("images/dk.jpg")
    dk1 = pygame.transform.scale(dk1, (100,100))
    dkd1 = pygame.image.load("images/dkd.jpg")
    dkd1 = pygame.transform.scale(dkd1, (100,100))
    dkCK1 = True

    # Link
    stock_link_1_2 = pygame.image.load("images/heartrojo.png")
    stock_link_1_2 = pygame.transform.scale(stock_link_1, (30,30))
    stock_link_2_2 = pygame.image.load("images/heartrojo.png")
    stock_link_2_2 = pygame.transform.scale(stock_link_2, (30,30))
    stock_link_3_2 = pygame.image.load("images/heartrojo.png")
    stock_link_3_2 = pygame.transform.scale(stock_link_3, (30,30))
    stock_link_4_2 = pygame.image.load("images/heartrojo.png")
    stock_link_4_2 = pygame.transform.scale(stock_link_4, (30,30))
    stock_link_55_2 = pygame.image.load("images/heartnegro.png")
    stock_link_55_2 = pygame.transform.scale(stock_link_55, (30,30))
    stock_link_66_2 = pygame.image.load("images/heartnegro.png")
    stock_link_66_2 = pygame.transform.scale(stock_link_66, (30,30))
    stock_link_77_2 = pygame.image.load("images/heartnegro.png")
    stock_link_77_2 = pygame.transform.scale(stock_link_77, (30,30))
    stock_link_88_2 = pygame.image.load("images/heartnegro.png")
    stock_link_88_2 = pygame.transform.scale(stock_link_88, (30,30))
    life_past_2 = pygame.image.load("images/lifepast.png")
    life_past_2 = pygame.transform.scale(life_past, (60,60))
    stock_link_1_CK_2 = True
    stock_link_2_CK_2 = True
    stock_link_3_CK_2 = True
    stock_link_4_CK_2 = True
    stock_link_55_CK_2 = True
    stock_link_66_CK_2 = True
    stock_link_77_CK_2 = True
    stock_link_88_CK_2 = True
    life_pastCK1 = True
    contador_link_2 = 4
    link1 = pygame.image.load("images/link.jpg")
    link1 = pygame.transform.scale(link1, (100,100))
    linkd1 = pygame.image.load("images/linkd.jpg")
    linkd1 = pygame.transform.scale(linkd1, (100,100))
    linkCK1 = True


    # Samus
    energy2 = pygame.image.load("images/energy0.png")
    energy2 = pygame.transform.scale(energy, (40,10))
    

    stock_samus_1_CK_2 = True
    stock_samus_2_CK_2 = True
    stock_samus_3_CK_2 = True
    stock_samus_4_CK_2 = True
    
    contador_samus_2 = 4
    samus1 = pygame.image.load("images/samus.jpg")
    samus1 = pygame.transform.scale(samus1, (100,100))
    samusd1 = pygame.image.load("images/samusd.jpg")
    samusd1 = pygame.transform.scale(samusd1, (100,100))
    samusCK1 = True
    energy2CK = True

    # C. Falcon
    stock_falcon_0_2 = pygame.image.load("images/fz_energy1.png")
    stock_falcon_0_2 = pygame.transform.scale(stock_falcon_0, (90,25))
    stock_falcon_1_2 = pygame.image.load("images/fz_energy2.png")
    stock_falcon_1_2 = pygame.transform.scale(stock_falcon_1, (85,20))
    stock_falcon_2_2 = pygame.image.load("images/fz_energy2.png")
    stock_falcon_2_2 = pygame.transform.scale(stock_falcon_1, (85,20))
    stock_falcon_3_2 = pygame.image.load("images/fz_energy2.png")
    stock_falcon_3_2 = pygame.transform.scale(stock_falcon_1, (85,20))
    stock_falcon_4_2 = pygame.image.load("images/fz_energy2.png")
    stock_falcon_4_2 = pygame.transform.scale(stock_falcon_1, (85,20))
    bar1_2 = pygame.image.load("images/bar1.png")
    bar1_2 = pygame.transform.scale(bar1, (56,2))
    bar2_2 = pygame.image.load("images/bar2.png")
    bar2_2 = pygame.transform.scale(bar2, (2,16))
    bar22CK_2 = True
    bar22CK_2_2 = True
    bar1CK_2 = True
    bar2CK_2 = True
    stock_falcon_0_CK_2 = True
    stock_falcon_1_CK_2 = True
    stock_falcon_2_CK_2 = True
    stock_falcon_3_CK_2 = True
    stock_falcon_4_CK_2 = True
    contador_falcon_2 = 4
    falcon1 = pygame.image.load("images/falcon2.jpg")
    falcon1 = pygame.transform.scale(falcon1, (100,100))
    falcond1 = pygame.image.load("images/falcond.jpg")
    falcond1 = pygame.transform.scale(falcond1, (100,100))
    falconCK1 = True

    # Ness
    stock_ness_1_2 = pygame.image.load("images/hp.png")
    stock_ness_1_2 = pygame.transform.scale(stock_ness_1, (19,17))
    stock_ness_2_2 = pygame.image.load("images/cero.png")
    stock_ness_2_2 = pygame.transform.scale(stock_ness_2, (17,17))
    stock_ness_3_2 = pygame.image.load("images/cero.png")
    stock_ness_3_2 = pygame.transform.scale(stock_ness_3, (17,17))
    stock_ness_4_2 = pygame.image.load("images/cero.png")
    stock_ness_4_2 = pygame.transform.scale(stock_ness_4, (17,17))
    stock_ness_5_2 = pygame.image.load("images/uno.png")
    stock_ness_5_2 = pygame.transform.scale(stock_ness_5, (17,17))
    stock_ness_6_2 = pygame.image.load("images/dos.png")
    stock_ness_6_2 = pygame.transform.scale(stock_ness_6, (17,17))
    stock_ness_7_2 = pygame.image.load("images/tres.png")
    stock_ness_7_2 = pygame.transform.scale(stock_ness_7, (17,17))
    stock_ness_8_2 = pygame.image.load("images/cuatro.png")
    stock_ness_8_2 = pygame.transform.scale(stock_ness_8, (17,17))
    stock_ness_1_CK_2 = True
    stock_ness_2_CK_2 = True
    stock_ness_3_CK_2 = True
    stock_ness_4_CK_2 = True
    stock_ness_5_CK_2 = False
    stock_ness_6_CK_2 = False
    stock_ness_7_CK_2 = False
    stock_ness_8_CK_2 = True
    contador_ness_2 = 4
    ness1 = pygame.image.load("images/ness.jpg")
    ness1 = pygame.transform.scale(ness1, (100,100))
    nessd1 = pygame.image.load("images/nessd.jpg")
    nessd1 = pygame.transform.scale(nessd1, (100,100))
    nessCK1 = True

    # Yoshi
    stock_yoshi_1_2 = pygame.image.load("images/egg.jpg")
    stock_yoshi_1_2 = pygame.transform.scale(stock_yoshi_1, (18,18))
    stock_yoshi_2_2 = pygame.image.load("images/egg.jpg")

    stock_yoshi_1_CK_2 = True
    stock_yoshi_2_CK_2 = True
    stock_yoshi_3_CK_2 = True
    stock_yoshi_4_CK_2 = True
    contador_yoshi_2 = 4
    yoshi1 = pygame.image.load("images/yoshi.jpg")
    yoshi1 = pygame.transform.scale(yoshi1, (100,100))
    yoshid1 = pygame.image.load("images/yoshid.jpg")
    yoshid1 = pygame.transform.scale(yoshid1, (100,100))
    yoshiCK1 = True

    # Kirby
    #stock_kirby_1_2 = pygame.image.load("images/tomato.png")
    #stock_kirby_1_2 = pygame.transform.scale(stock_kirby_1, (30,30))

    stock_kirby_1_CK_2 = True
    stock_kirby_2_CK_2 = True
    stock_kirby_3_CK_2 = True
    stock_kirby_4_CK_2 = True
    contador_kirby_2 = 4
    kirby1 = pygame.image.load("images/kirby.jpg")
    kirby1 = pygame.transform.scale(kirby1, (100,100))
    kirbyd1 = pygame.image.load("images/kirbyd.jpg")
    kirbyd1 = pygame.transform.scale(kirbyd1, (100,100))
    kirbyCK1 = True

    # Fox
    
    stock_fox_1_CK_2 = True
    stock_fox_2_CK_2 = True
    stock_fox_3_CK_2 = True
    stock_fox_4_CK_2 = True
    contador_fox_2 = 4
    fox1 = pygame.image.load("images/fox.jpg")
    fox1 = pygame.transform.scale(fox1, (100,100))
    foxd1 = pygame.image.load("images/foxd.jpg")
    foxd1 = pygame.transform.scale(foxd1, (100,100))
    foxCK1 = True

    # Pikachu
    
    stock_pikachu_1_CK_2 = True
    stock_pikachu_2_CK_2 = True
    stock_pikachu_3_CK_2 = True
    stock_pikachu_4_CK_2 = True
    contador_pikachu_2 = 4
    pikachu1 = pygame.image.load("images/pikachu.jpg")
    pikachu1 = pygame.transform.scale(pikachu1, (100,100))
    pikachud1 = pygame.image.load("images/pikachud.jpg")
    pikachud1 = pygame.transform.scale(pikachud1, (100,100))
    pikachuCK1 = True

    # Jigglypuff
    
    stock_jigglypuff_1_CK_2 = True
    stock_jigglypuff_2_CK_2 = True
    stock_jigglypuff_3_CK_2 = True
    stock_jigglypuff_4_CK_2 = True
    contador_jigglypuff_2 = 4
    jigglypuff1 = pygame.image.load("images/jigglypuff.jpg")
    jigglypuff1 = pygame.transform.scale(jigglypuff1, (100,100))
    jigglypuffd1 = pygame.image.load("images/jigglypuffd.jpg")
    jigglypuffd1 = pygame.transform.scale(jigglypuffd1, (100,100))
    jigglypuffCK1 = True

    negro = (0,0,0)

    # Mouse
    cursor = pygame.image.load("images/fan.png")
    cursor = pygame.transform.scale(cursor, (40,40))
    pygame.mouse.set_visible(False)
    coord = pygame.mouse.get_pos()

    # Boton Reset
    reset = pygame.image.load("images/reset.png")
    reset = pygame.transform.scale(reset, (90,60))
    resetCK = True

    # Choose a Mode
    modo = pygame.image.load("images/mode.png")
    #modo = pygame.transform.scale(modo, (300,200))
    modoCK = True

    # 1) Escoger opcion
    opc = True
    opc_1 = False
    opc_2 = False

    # 2) Escoger opcion 
    carta_1 = pygame.image.load("images/carta_1.png")
    carta_1 = pygame.transform.scale(carta_1, (160, 220))
    carta_1CK = True
    s_vanilla = pygame.image.load("images/svanilla.png")
    s_vanilla = pygame.transform.scale(s_vanilla, (190, 100))
    s_remix = pygame.image.load("images/sremix.png")
    s_remix = pygame.transform.scale(s_remix, (150, 120))
    s_vanilla1 = pygame.image.load("images/svanilla.png")
    s_vanilla1 = pygame.transform.scale(s_vanilla1, (150, 70))
    s_remix1 = pygame.image.load("images/sremix.png")
    s_remix1 = pygame.transform.scale(s_remix1, (120, 90))
    plus = pygame.image.load("images/plus.png")
    plus = pygame.transform.scale(plus,(110,70))
    s_vanillaCK = True
    s_remixCK = True
    s_vanillaCK1 = True
    s_remixCK1 = True
    plusCK = True

    # Boton start 
    start_b = pygame.image.load("images/startb.png")
    start_b = pygame.transform.scale(start_b, (80,40))
    start_bCK = True
    start_b2 = pygame.image.load("images/startb2.png")
    start_b2 = pygame.transform.scale(start_b2, (80,40))
    start_bCK2 = False
    
    clock = pygame.time.Clock()

    # Smash Remix Creation
    
    
    #----------------------------------------------------------------
    #------------Accion de mostrar y no la imagen---------------
    #----------------------------------------------------------------

    
    while True:

        # Menu
        if modoCK == True:
            ventana.blit(modo,(0,0))

            if s_vanillaCK == True:
                ventana.blit(s_vanilla, (70,300))

            if s_remixCK == True:
                ventana.blit(s_remix, (320,300))

            if s_vanillaCK1 == True:
                ventana.blit(s_vanilla1, (540,280))

            if s_remixCK1 == True:
                ventana.blit(s_remix1, (640,340))

            if plusCK == True:
                ventana.blit(plus, (590,320))

            # Mostrar mouse
            cor = pygame.mouse.get_pos()
            ventana.blit(cursor, cor)            

        
        if start_bCK == True:
            ventana.blit(start_b, (130, 500))
            #ventana.blit(start_b, (355, 500))
            #ventana.blit(start_b, (600, 500))
            # Mostrar mouse
            cor = pygame.mouse.get_pos()
            ventana.blit(cursor, cor)
        else:
            ventana.blit(start_b, (-400, -400))
            #ventana.blit(start_b, (-400, -400))
            #ventana.blit(start_b, (-400, -400))
            # Mostrar mouse
            cor = pygame.mouse.get_pos()
            ventana.blit(cursor, cor)

        
        # Opcion 1
        if opc_1 == True:
            
            ventana.fill(negro)
        
            if resetCK == True:
                ventana.blit(reset,(360,570))

        
            
            
            #---------------------------------------------------------------
            #---------------------------------------------------------------
            #---------------------------------------------------------------
            # Fila 1 
            
            # Luigi
            if luigiCK == True:
                ventana.blit(luigi,(0,0))
            else:
                ventana.blit(luigid,(0,0))

            if stock_luigi_1_CK == True:
                ventana.blit(stock_luigi_1, (10,80))
                 
            else:
                ventana.blit(stock_luigi_1, (-40,-40))
                

            if stock_luigi_2_CK == True:
                ventana.blit(stock_luigi_1, (30,80))
            
            else:
                ventana.blit(stock_luigi_1, (-40,-40))
                

            if stock_luigi_3_CK == True:
                ventana.blit(stock_luigi_1, (50,80))
                
            else:
                ventana.blit(stock_luigi_1, (-40,-40))
                
                
            if stock_luigi_4_CK == True:
                ventana.blit(stock_luigi_1, (70,80))
                
            else:
                ventana.blit(stock_luigi_1, (-40,-40))
                
            

            # Mario
            if marioCK == True:
                ventana.blit(mario,(0,100))
            else:
                ventana.blit(mariod,(0,100))

            if stock_mario_1_CK == True:
                ventana.blit(stock_mario_1, (10,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))

            if stock_mario_2_CK == True:
                ventana.blit(stock_mario_1, (30,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))

            if stock_mario_3_CK == True:
                ventana.blit(stock_mario_1, (50,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))
                
            if stock_mario_4_CK == True:
                ventana.blit(stock_mario_1, (70,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))

                
            # DK
            if dkCK == True:
                ventana.blit(dk,(0,200))
            else:
                ventana.blit(dkd,(0,200))

            if stock_dk_1_CK == True:
                ventana.blit(stock_dk_1, (8,275))
            else:
                ventana.blit(stock_dk_1, (-40,-40))

            if stock_dk_2_CK == True:
                ventana.blit(stock_dk_1, (28,275))
            else:
                ventana.blit(stock_dk_1, (-40,-40))

            if stock_dk_3_CK == True:
                ventana.blit(stock_dk_1, (48,275))
            else:
                ventana.blit(stock_dk_1, (-40,-40))
                
            if stock_dk_4_CK == True:
                ventana.blit(stock_dk_1, (68,275))
            else:
                ventana.blit(stock_dk_1, (-40,-40))


            # Link
            if linkCK == True:
                ventana.blit(link,(0,300))
            else:
                ventana.blit(linkd,(0,300))

            if stock_link_1_CK == True:
                ventana.blit(stock_link_1, (4,374))
            else:
                ventana.blit(stock_link_1, (-40,-40))
                ventana.blit(stock_link_55, (4,375))
                

            if stock_link_2_CK == True:
                ventana.blit(stock_link_2, (24,374))
            else:
                ventana.blit(stock_link_2, (-40,-40))
                ventana.blit(stock_link_66, (24,375))
                

            if stock_link_3_CK == True:
                ventana.blit(stock_link_3, (44,374))
            else:
                ventana.blit(stock_link_3, (-40,-40))
                ventana.blit(stock_link_77, (44,375))
                
                
            if stock_link_4_CK == True:
                ventana.blit(stock_link_4, (64,374))
            else:
                ventana.blit(stock_link_4, (-40,-40))
                ventana.blit(stock_link_88, (64,375))

            if life_pastCK == True:
                ventana.blit(life_past, (20, 350))
            else:
                ventana.blit(life_past, (20, 350))

            
            # Samus
            if samusCK == True:
                ventana.blit(samus,(0,400))
            else:
                ventana.blit(samusd,(0,400))

            if stock_samus_1_CK == True:
                ventana.blit(stock_samus_1, (14,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (14,480))

            if stock_samus_2_CK == True:
                ventana.blit(stock_samus_1, (30,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (30,480))

            if stock_samus_3_CK == True:
                ventana.blit(stock_samus_1, (46,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (46,480))
                
            if stock_samus_4_CK == True:
                ventana.blit(stock_samus_1, (62,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (62,480))

            if energyCK == True:
                ventana.blit(energy, (14,490))
            else:
                ventana.blit(energy, (14,490))


            # C. Falcon
            if falconCK == True:
                ventana.blit(falcon,(0,500))
            else:
                ventana.blit(falcond,(0,500))

            if stock_falcon_0_CK == True:
                ventana.blit(stock_falcon_0, (5,575))
            else:
                ventana.blit(stock_falcon_0, (-40,-40))
            
            if stock_falcon_1_CK == True:
                ventana.blit(stock_falcon_1, (6,580))
            else:
                ventana.blit(stock_falcon_1, (-40,-40))

            if stock_falcon_2_CK == True:
                ventana.blit(stock_falcon_1, (20,580))
            else:
                ventana.blit(stock_falcon_1, (-40,-40))

            if stock_falcon_3_CK == True:
                ventana.blit(stock_falcon_1, (34,580))
            else:
                ventana.blit(stock_falcon_1, (-40,-40))
                
            if stock_falcon_4_CK == True:
                ventana.blit(stock_falcon_1, (48,580))
            else:
                ventana.blit(stock_falcon_1, (-40,-40))

            if bar1CK == True:
                ventana.blit(bar1, (35,581))
            else:
                ventana.blit(bar1, (35,581))

            if bar2CK == True:
                ventana.blit(bar1, (35,597))
            else:
                ventana.blit(bar1, (35,597))

            if bar22CK == True:
                ventana.blit(bar2, (35,583))
            else:
                ventana.blit(bar2, (35,583))

            if bar22CK_2 == True:
                ventana.blit(bar2, (89,582))
            

            # Ness
            if nessCK == True:
                ventana.blit(ness,(100,0))
            else:
                ventana.blit(nessd,(100,0))

            if stock_ness_1_CK == True:
                ventana.blit(stock_ness_1, (110,80))
            else:
                ventana.blit(stock_ness_1, (110,80))

            if stock_ness_2_CK == True:
                ventana.blit(stock_ness_2, (133,80))
            else:
                ventana.blit(stock_ness_2, (133,80))

            if stock_ness_3_CK == True:
                ventana.blit(stock_ness_3, (150,80))
            else:
                ventana.blit(stock_ness_3, (150,80))
                
            if stock_ness_4_CK == True:
                ventana.blit(stock_ness_4, (167,80))
            else:
                ventana.blit(stock_ness_4, (167,80))

            if stock_ness_5_CK == True:
                ventana.blit(stock_ness_5, (167,80))
            else:
                ventana.blit(stock_ness_5, (-40,-40))

            if stock_ness_6_CK == True:
                ventana.blit(stock_ness_6, (167,80))
            else:
                ventana.blit(stock_ness_6, (-40,-40))

            if stock_ness_7_CK == True:
                ventana.blit(stock_ness_7, (167,80))
            else:
                ventana.blit(stock_ness_7, (-40,-40))
                
            if stock_ness_8_CK == True:
                ventana.blit(stock_ness_8, (167,80))
            else:
                ventana.blit(stock_ness_8, (-40,-40))

            
            # Yoshi
            if yoshiCK == True:
                ventana.blit(yoshi,(100,100))
            else:
                ventana.blit(yoshid,(100,100))

            if stock_yoshi_1_CK == True:
                ventana.blit(stock_yoshi_1, (110,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))

            if stock_yoshi_2_CK == True:
                ventana.blit(stock_yoshi_1, (130,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))

            if stock_yoshi_3_CK == True:
                ventana.blit(stock_yoshi_1, (150,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))
                
            if stock_yoshi_4_CK == True:
                ventana.blit(stock_yoshi_1, (170,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))
            

            # Kirby
            if kirbyCK == True:
                ventana.blit(kirby,(100,200))
            else:
                ventana.blit(kirbyd,(100,200))

            if stock_kirby_1_CK == True:
                ventana.blit(stock_kirby_1, (105,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))

            if stock_kirby_2_CK == True:
                ventana.blit(stock_kirby_1, (125,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))

            if stock_kirby_3_CK == True:
                ventana.blit(stock_kirby_1, (145,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))
                
            if stock_kirby_4_CK == True:
                ventana.blit(stock_kirby_1, (165,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))
            

            # Fox
            if foxCK == True:
                ventana.blit(fox,(100,300))
            else:
                ventana.blit(foxd,(100,300))

            if stock_fox_1_CK == True:
                ventana.blit(stock_fox_1, (110,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))

            if stock_fox_2_CK == True:
                ventana.blit(stock_fox_1, (130,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))

            if stock_fox_3_CK == True:
                ventana.blit(stock_fox_1, (150,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))
                
            if stock_fox_4_CK == True:
                ventana.blit(stock_fox_1, (170,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))
            

            # Pikachu
            if pikachuCK == True:
                ventana.blit(pikachu,(100,400))
            else:
                ventana.blit(pikachud,(100,400))

            if stock_pikachu_1_CK == True:
                ventana.blit(stock_pikachu_1, (110,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))

            if stock_pikachu_2_CK == True:
                ventana.blit(stock_pikachu_1, (130,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))

            if stock_pikachu_3_CK == True:
                ventana.blit(stock_pikachu_1, (150,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))
                
            if stock_pikachu_4_CK == True:
                ventana.blit(stock_pikachu_1, (170,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))
                

            # Jigglypuff
            if jigglypuffCK == True:
                ventana.blit(jigglypuff,(100,500))
            else:
                ventana.blit(jigglypuffd,(100,500))

            if stock_jigglypuff_1_CK == True:
                ventana.blit(stock_jigglypuff_1, (110,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))

            if stock_jigglypuff_2_CK == True:
                ventana.blit(stock_jigglypuff_1, (130,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))

            if stock_jigglypuff_3_CK == True:
                ventana.blit(stock_jigglypuff_1, (150,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))
                
            if stock_jigglypuff_4_CK == True:
                ventana.blit(stock_jigglypuff_1, (170,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))
            
            #----------------------------------------------------------
            #----------------------------------------------------------
            #----------------------------------------------------------
            # Fila 2

            # Luigi
            if luigiCK1 == True:
                ventana.blit(luigi,(600,0))
            else:
                ventana.blit(luigid,(600,0))

            if stock_luigi_1_CK_2 == True:
                ventana.blit(stock_luigi_1, (610,80))
            else:
                ventana.blit(stock_luigi_1, (-40,-40))

            if stock_luigi_2_CK_2 == True:
                ventana.blit(stock_luigi_1, (630,80))
            else:
                ventana.blit(stock_luigi_1, (-40,-40))

            if stock_luigi_3_CK_2 == True:
                ventana.blit(stock_luigi_1, (650,80))
            else:
                ventana.blit(stock_luigi_1, (-40,-40))
                
            if stock_luigi_4_CK_2 == True:
                ventana.blit(stock_luigi_1, (670,80))
            else:
                ventana.blit(stock_luigi_1, (-40,-40))
            

            # Mario
            if marioCK1 == True:
                ventana.blit(mario,(600,100))
            else:
                ventana.blit(mariod,(600,100))

            if stock_mario_1_CK_2 == True:
                ventana.blit(stock_mario_1, (610,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))

            if stock_mario_2_CK_2 == True:
                ventana.blit(stock_mario_1, (630,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))

            if stock_mario_3_CK_2 == True:
                ventana.blit(stock_mario_1, (650,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))
                
            if stock_mario_4_CK_2 == True:
                ventana.blit(stock_mario_1, (670,180))
            else:
                ventana.blit(stock_mario_1, (-40,-40))
                
            
            # DK
            if dkCK1 == True:
                ventana.blit(dk1,(600,200))
            else:
                ventana.blit(dkd1,(600,200))

            if stock_dk_1_CK_2 == True:
                ventana.blit(stock_dk_1_2, (608,275))
            else:
                ventana.blit(stock_dk_1_2, (-40,-40))

            if stock_dk_2_CK_2 == True:
                ventana.blit(stock_dk_2_2, (628,275))
            else:
                ventana.blit(stock_dk_2_2, (-40,-40))

            if stock_dk_3_CK_2 == True:
                ventana.blit(stock_dk_3_2, (648,275))
            else:
                ventana.blit(stock_dk_3_2, (-40,-40))
                
            if stock_dk_4_CK_2 == True:
                ventana.blit(stock_dk_4_2, (668,275))
            else:
                ventana.blit(stock_dk_4_2, (-40,-40))

                
            # Link
            if linkCK1 == True:
                ventana.blit(link1,(600,300))
            else:
                ventana.blit(linkd1,(600,300))

            if stock_link_1_CK_2 == True:
                ventana.blit(stock_link_1_2, (604,374))
            else:
                ventana.blit(stock_link_1_2, (-40,-40))
                ventana.blit(stock_link_55_2, (604,375))

            if stock_link_2_CK_2 == True:
                ventana.blit(stock_link_2_2, (624,374))
            else:
                ventana.blit(stock_link_2_2, (-40,-40))
                ventana.blit(stock_link_66_2, (624,375))

            if stock_link_3_CK_2 == True:
                ventana.blit(stock_link_3_2, (644,374))
            else:
                ventana.blit(stock_link_3_2, (-40,-40))
                ventana.blit(stock_link_77_2, (644,375))
                
            if stock_link_4_CK_2 == True:
                ventana.blit(stock_link_4_2, (664,374))
            else:
                ventana.blit(stock_link_4_2, (-40,-40))
                ventana.blit(stock_link_88_2, (664,375))

            if life_pastCK1 == True:
                ventana.blit(life_past_2, (620, 350))
            else:
                ventana.blit(life_past_2, (620, 350))


            # Samus
            if samusCK1 == True:
                ventana.blit(samus1,(600,400))
            else:
                ventana.blit(samusd1,(600,400))

            if stock_samus_1_CK_2 == True:
                ventana.blit(stock_samus_1, (614,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (614,480))

            if stock_samus_2_CK_2 == True:
                ventana.blit(stock_samus_1, (630,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (630,480))

            if stock_samus_3_CK_2 == True:
                ventana.blit(stock_samus_1, (646,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (646,480))
                
            if stock_samus_4_CK_2 == True:
                ventana.blit(stock_samus_1, (662,480))
            else:
                ventana.blit(stock_samus_1, (-40,-40))
                ventana.blit(stock_samus_5, (662,480))

            if energy2CK == True:
                ventana.blit(energy2, (614,490))
            else:
                ventana.blit(energy2, (614,490))

            
            # Falcon
            if falconCK1 == True:
                ventana.blit(falcon1,(600,500))
            else:
                ventana.blit(falcond1,(600,500))

            if stock_falcon_0_CK_2 == True:
                ventana.blit(stock_falcon_0_2, (605,575))
            else:
                ventana.blit(stock_falcon_0_2, (-40,-40))
            
            if stock_falcon_1_CK_2 == True:
                ventana.blit(stock_falcon_1_2, (606,580))
            else:
                ventana.blit(stock_falcon_1_2, (-40,-40))

            if stock_falcon_2_CK_2 == True:
                ventana.blit(stock_falcon_2_2, (620,580))
            else:
                ventana.blit(stock_falcon_2_2, (-40,-40))

            if stock_falcon_3_CK_2 == True:
                ventana.blit(stock_falcon_3_2, (634,580))
            else:
                ventana.blit(stock_falcon_3_2, (-40,-40))
                
            if stock_falcon_4_CK_2 == True:
                ventana.blit(stock_falcon_4_2, (648,580))
            else:
                ventana.blit(stock_falcon_4_2, (-40,-40))

            if bar1CK_2 == True:
                ventana.blit(bar1_2, (635,581))
            else:
                ventana.blit(bar1_2, (635,581))

            if bar2CK_2 == True:
                ventana.blit(bar1_2, (635,597))
            else:
                ventana.blit(bar1_2, (635,597))

            if bar22CK_2 == True:
                ventana.blit(bar2_2, (635,583))
            else:
                ventana.blit(bar2_2, (635,583))

            if bar22CK_2_2 == True:
                ventana.blit(bar2_2, (689,582))
            


            # Ness
            if nessCK1 == True:
                ventana.blit(ness1,(700,0))
            else:
                ventana.blit(nessd1,(700,0))

            if stock_ness_1_CK_2 == True:
                ventana.blit(stock_ness_1_2, (710,80))
            else:
                ventana.blit(stock_ness_1_2, (710,80))

            if stock_ness_2_CK_2 == True:
                ventana.blit(stock_ness_2_2, (733,80))
            else:
                ventana.blit(stock_ness_2_2, (733,80))

            if stock_ness_3_CK_2 == True:
                ventana.blit(stock_ness_3_2, (750,80))
            else:
                ventana.blit(stock_ness_3_2, (750,80))
                
            if stock_ness_4_CK_2 == True:
                ventana.blit(stock_ness_4_2, (767,80))
            else:
                ventana.blit(stock_ness_4_2, (767,80))

            if stock_ness_5_CK_2 == True:
                ventana.blit(stock_ness_5_2, (767,80))
            else:
                ventana.blit(stock_ness_5_2, (-40,-40))

            if stock_ness_6_CK_2 == True:
                ventana.blit(stock_ness_6_2, (767,80))
            else:
                ventana.blit(stock_ness_6_2, (-40,-40))

            if stock_ness_7_CK_2 == True:
                ventana.blit(stock_ness_7_2, (767,80))
            else:
                ventana.blit(stock_ness_7_2, (-40,-40))
                
            if stock_ness_8_CK_2 == True:
                ventana.blit(stock_ness_8_2, (767,80))
            else:
                ventana.blit(stock_ness_8_2, (-40,-40))


            # Yoshi
            if yoshiCK1 == True:
                ventana.blit(yoshi1,(700,100))
            else:
                ventana.blit(yoshid1,(700,100))

            if stock_yoshi_1_CK_2 == True:
                ventana.blit(stock_yoshi_1, (710,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))

            if stock_yoshi_2_CK_2 == True:
                ventana.blit(stock_yoshi_1, (730,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))

            if stock_yoshi_3_CK_2 == True:
                ventana.blit(stock_yoshi_1, (750,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))
                
            if stock_yoshi_4_CK_2 == True:
                ventana.blit(stock_yoshi_1, (770,180))
            else:
                ventana.blit(stock_yoshi_1, (-40,-40))
            
            
            # Kirby
            if kirbyCK1 == True:
                ventana.blit(kirby1,(700,200))
            else:
                ventana.blit(kirbyd1,(700,200))

            if stock_kirby_1_CK_2 == True:
                ventana.blit(stock_kirby_1, (705,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))

            if stock_kirby_2_CK_2 == True:
                ventana.blit(stock_kirby_1, (725,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))

            if stock_kirby_3_CK_2 == True:
                ventana.blit(stock_kirby_1, (745,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))
                
            if stock_kirby_4_CK_2 == True:
                ventana.blit(stock_kirby_1, (765,270))
            else:
                ventana.blit(stock_kirby_1, (-40,-40))

            
            # Fox
            if foxCK1 == True:
                ventana.blit(fox1,(700,300))
            else:
                ventana.blit(foxd1,(700,300))

            if stock_fox_1_CK_2 == True:
                ventana.blit(stock_fox_1, (710,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))

            if stock_fox_2_CK_2 == True:
                ventana.blit(stock_fox_1, (730,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))

            if stock_fox_3_CK_2 == True:
                ventana.blit(stock_fox_1, (750,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))
                
            if stock_fox_4_CK_2 == True:
                ventana.blit(stock_fox_1, (770,378))
            else:
                ventana.blit(stock_fox_1, (-40,-40))

            
            # Pikachu
            if pikachuCK1 == True:
                ventana.blit(pikachu1,(700,400))
            else:
                ventana.blit(pikachud1,(700,400))

            if stock_pikachu_1_CK_2 == True:
                ventana.blit(stock_pikachu_1, (710,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))

            if stock_pikachu_2_CK_2 == True:
                ventana.blit(stock_pikachu_1, (730,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))

            if stock_pikachu_3_CK_2 == True:
                ventana.blit(stock_pikachu_1, (750,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))
                
            if stock_pikachu_4_CK_2 == True:
                ventana.blit(stock_pikachu_1, (770,480))
            else:
                ventana.blit(stock_pikachu_1, (-40,-40))

            
            # Jigglypuff
            if jigglypuffCK1 == True:
                ventana.blit(jigglypuff1,(700,500))
            else:
                ventana.blit(jigglypuffd1,(700,500))

            if stock_jigglypuff_1_CK_2 == True:
                ventana.blit(stock_jigglypuff_1, (710,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))

            if stock_jigglypuff_2_CK_2 == True:
                ventana.blit(stock_jigglypuff_1, (730,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))

            if stock_jigglypuff_3_CK_2 == True:
                ventana.blit(stock_jigglypuff_1, (750,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))
                
            if stock_jigglypuff_4_CK_2 == True:
                ventana.blit(stock_jigglypuff_1, (770,580))
            else:
                ventana.blit(stock_jigglypuff_1, (-40,-40))
            

            if textoCK == True:
                texto3 = str(cont_texto)
                texto_3 = myfont_stocks.render(texto3,False,(255,255,255))
                ventana.blit(texto_3,(83,597))
            else:
                ventana.blit(texto_3,(83,597))

            if texto2CK == True:
                texto3 = str(cont_texto2)
                texto_4 = myfont_stocks.render(texto3,False,(255,255,255))
                ventana.blit(texto_4,(683,597))
            else:
                ventana.blit(texto_4,(683,597))

            
                
            
            # Mostrar version del programa y los creadores
            
            ventana.blit(texto_2,(696,633))
            
            
            # Mostrar mouse
            cor = pygame.mouse.get_pos()
            ventana.blit(cursor, cor)


        # Opcion 2 REMIX CHARACTERS---------------------------------------------
        #-----------------------------------------------------------------------
        #-----------------------------------------------------------------------

        if opc_2 == True:
            
            ventana.fill(negro)

            # FILA 1------------------------------------------------------------

            if remix_char.dr_marioCK == True:
                ventana.blit(remix_char.dr_mario, (0,0))

            if remix_char.y_linkCK == True:
                ventana.blit(remix_char.y_link, (0,100))

            if remix_char.dark_samusCK == True:
                ventana.blit(remix_char.dark_samus, (0,200))

            if remix_char.warioCK == True:
                ventana.blit(remix_char.wario, (0,300))

            if remix_char.lucasCK == True:
                ventana.blit(remix_char.lucas, (0,400))

            if remix_char.ganondorfCK == True:
                ventana.blit(remix_char.ganondorf, (0,500))

            if remix_char.falcooCK == True:
                ventana.blit(remix_char.falcoo, (100,0))


            # FILA 2------------------------------------------------------------

            if remix_char.dr_marioCK2 == True:
                ventana.blit(remix_char.dr_mario, (600,0))

            if remix_char.y_linkCK2 == True:
                ventana.blit(remix_char.y_link, (600,100))

            if remix_char.dark_samusCK2 == True:
                ventana.blit(remix_char.dark_samus, (600,200))

            if remix_char.warioCK2 == True:
                ventana.blit(remix_char.wario, (600,300))

            if remix_char.lucasCK2 == True:
                ventana.blit(remix_char.lucas, (600,400))

            if remix_char.ganondorfCK2 == True:
                ventana.blit(remix_char.ganondorf, (600,500))

            if remix_char.falcooCK2 == True:
                ventana.blit(remix_char.falcoo, (700,0))

            # Mostrar Mouse
            cor = pygame.mouse.get_pos()
            ventana.blit(cursor, cor)

            
                
                
            
            #-----------------------------------------------------------
            #-----------------------------------------------------------
            #-----------------------------------------------------------
            # Eventos del programa (loop)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                
                
                if opc == True:
                    
                    if event.type == MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        
                        
                        if x > 100 and x < 182:
                            if y > 460 and y < 500:
                                start_bCK = False
                                
                                #pause_time = int(pygame.time.get_ticks()/1000)
                                #print(pause_time)
                                #display(2,pause_time)
                                
                                modoCK = False
                                opc = False
                                opc_1 = True

                        if x > 325 and x < 405:
                            if y > 460 and y < 500:
                                modoCK = False
                                opc_2 = True
                                

                        


                
                
                
                if opc_1 == True:
                    
                    
                        
                    
                    #display(5)
                    
                        
                    if event.type == MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()

                        
                        
                        
                        if my > 535 and my < 570:
                            if mx > 300 and mx < 420:
                                
                                cont_texto = 48
                                cont_texto2 = 48
                                
                                stock_luigi_1_CK = True
                                stock_luigi_2_CK = True
                                stock_luigi_3_CK = True
                                stock_luigi_4_CK = True
                                luigiCK = True
                                contador_luigi = 4

                                stock_mario_1_CK = True
                                stock_mario_2_CK = True
                                stock_mario_3_CK = True
                                stock_mario_4_CK = True
                                marioCK = True
                                contador_mario = 4

                                stock_dk_1_CK = True
                                stock_dk_2_CK = True
                                stock_dk_3_CK = True
                                stock_dk_4_CK = True
                                dkCK = True
                                contador_dk = 4

                                stock_link_1_CK = True
                                stock_link_2_CK = True
                                stock_link_3_CK = True
                                stock_link_4_CK = True
                                linkCK = True
                                contador_link = 4

                                stock_samus_1_CK = True
                                stock_samus_2_CK = True
                                stock_samus_3_CK = True
                                stock_samus_4_CK = True
                                samusCK = True
                                contador_samus = 4

                                stock_falcon_1_CK = True
                                stock_falcon_2_CK = True
                                stock_falcon_3_CK = True
                                stock_falcon_4_CK = True
                                falconCK = True
                                contador_falcon = 4

                                stock_ness_4_CK = False
                                stock_ness_8_CK = True
                                nessCK = True
                                
                                contador_ness = 4

                                stock_yoshi_1_CK = True
                                stock_yoshi_2_CK = True
                                stock_yoshi_3_CK = True
                                stock_yoshi_4_CK = True
                                yoshiCK = True
                                contador_yoshi = 4

                                stock_kirby_1_CK = True
                                stock_kirby_2_CK = True
                                stock_kirby_3_CK = True
                                stock_kirby_4_CK = True
                                kirbyCK = True
                                contador_kirby = 4

                                stock_fox_1_CK = True
                                stock_fox_2_CK = True
                                stock_fox_3_CK = True
                                stock_fox_4_CK = True
                                foxCK = True
                                contador_fox = 4

                                stock_pikachu_1_CK = True
                                stock_pikachu_2_CK = True
                                stock_pikachu_3_CK = True
                                stock_pikachu_4_CK = True
                                pikachuCK = True
                                contador_pikachu = 4

                                stock_jigglypuff_1_CK = True
                                stock_jigglypuff_2_CK = True
                                stock_jigglypuff_3_CK = True
                                stock_jigglypuff_4_CK = True
                                jigglypuffCK = True
                                contador_jigglypuff = 4

                                # Fila 2

                                stock_luigi_1_CK_2 = True
                                stock_luigi_2_CK_2 = True
                                stock_luigi_3_CK_2 = True
                                stock_luigi_4_CK_2 = True
                                luigiCK1 = True
                                contador_luigi_2 = 4

                                stock_mario_1_CK_2 = True
                                stock_mario_2_CK_2 = True
                                stock_mario_3_CK_2 = True
                                stock_mario_4_CK_2 = True
                                marioCK1 = True
                                contador_mario_2 = 4

                                stock_dk_1_CK_2 = True
                                stock_dk_2_CK_2 = True
                                stock_dk_3_CK_2 = True
                                stock_dk_4_CK_2 = True
                                dkCK1 = True
                                contador_dk_2 = 4

                                stock_link_1_CK_2 = True
                                stock_link_2_CK_2 = True
                                stock_link_3_CK_2 = True
                                stock_link_4_CK_2 = True
                                linkCK1 = True
                                contador_link_2 = 4

                                stock_samus_1_CK_2 = True
                                stock_samus_2_CK_2 = True
                                stock_samus_3_CK_2 = True
                                stock_samus_4_CK_2 = True
                                samusCK1 = True
                                contador_samus_2 = 4

                                stock_falcon_1_CK_2 = True
                                stock_falcon_2_CK_2 = True
                                stock_falcon_3_CK_2 = True
                                stock_falcon_4_CK_2 = True
                                falconCK1 = True
                                contador_falcon_2 = 4

                                stock_ness_4_CK_2 = False
                                stock_ness_8_CK_2 = True
                                nessCK1 = True
                                
                                contador_ness_2 = 4

                                stock_yoshi_1_CK_2 = True
                                stock_yoshi_2_CK_2 = True
                                stock_yoshi_3_CK_2 = True
                                stock_yoshi_4_CK_2 = True
                                yoshiCK1 = True
                                contador_yoshi_2 = 4

                                stock_kirby_1_CK_2 = True
                                stock_kirby_2_CK_2 = True
                                stock_kirby_3_CK_2 = True
                                stock_kirby_4_CK_2 = True
                                kirbyCK1 = True
                                contador_kirby_2 = 4

                                stock_fox_1_CK_2 = True
                                stock_fox_2_CK_2 = True
                                stock_fox_3_CK_2 = True
                                stock_fox_4_CK_2 = True
                                foxCK1 = True
                                contador_fox_2 = 4

                                stock_pikachu_1_CK_2 = True
                                stock_pikachu_2_CK_2 = True
                                stock_pikachu_3_CK_2 = True
                                stock_pikachu_4_CK_2 = True
                                pikachuCK1 = True
                                contador_pikachu_2 = 4

                                stock_jigglypuff_1_CK_2 = True
                                stock_jigglypuff_2_CK_2 = True
                                stock_jigglypuff_3_CK_2 = True
                                stock_jigglypuff_4_CK_2 = True
                                jigglypuffCK1 = True
                                contador_jigglypuff_2 = 4

                                
                                
                                

                      #-------------------------------------------          
                        
                        # Fila 1
                        
                        # Luigi
                        if mx < 100 and my < 100:
                            contador_luigi = contador_luigi - 1
                            
                            
                            if contador_luigi == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_luigi_4_CK = False
                                
                            if contador_luigi == 2:
                                cont_texto = cont_texto - 1
                                stock_luigi_3_CK = False
                                textoCK = True

                            if contador_luigi == 1:
                                cont_texto = cont_texto - 1
                                stock_luigi_2_CK = False
                                textoCK = True

                            if contador_luigi == 0:
                                cont_texto = cont_texto - 1
                                stock_luigi_1_CK = False
                                textoCK = True
                                luigiCK = False
                                

                            if contador_luigi == -1:
                                cont_texto = cont_texto + 4
                                stock_luigi_1_CK = True
                                stock_luigi_2_CK = True
                                stock_luigi_3_CK = True
                                stock_luigi_4_CK = True
                                luigiCK = True
                                contador_luigi = 4
                                

                                


                        # Mario
                        if mx < 100 and my > 100 and my < 200:
                            contador_mario = contador_mario - 1
                            
                            if contador_mario == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_mario_4_CK = False
                                

                            if contador_mario == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_mario_3_CK = False

                            if contador_mario == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_mario_2_CK = False

                            if contador_mario == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_mario_1_CK = False
                                marioCK = False

                            if contador_mario == -1:
                                cont_texto = cont_texto + 4
                                stock_mario_1_CK = True
                                stock_mario_2_CK = True
                                stock_mario_3_CK = True
                                stock_mario_4_CK = True
                                marioCK = True
                                contador_mario = 4


                        # DK
                        if mx < 100 and my > 200 and my < 300:
                            contador_dk = contador_dk - 1
                            
                            if contador_dk == 3:
                                stock_dk_4_CK = False
                                cont_texto = cont_texto - 1
                                textoCK = True

                            if contador_dk == 2:
                                stock_dk_3_CK = False
                                cont_texto = cont_texto - 1
                                textoCK = True

                            if contador_dk == 1:
                                stock_dk_2_CK = False
                                cont_texto = cont_texto - 1
                                textoCK = True

                            if contador_dk == 0:
                                stock_dk_1_CK = False
                                dkCK = False
                                cont_texto = cont_texto - 1
                                textoCK = True

                            if contador_dk == -1:
                                cont_texto = cont_texto + 4
                                stock_dk_1_CK = True
                                stock_dk_2_CK = True
                                stock_dk_3_CK = True
                                stock_dk_4_CK = True
                                dkCK = True
                                contador_dk = 4


                        # Link
                        if mx < 100 and my > 300 and my < 400:
                            contador_link = contador_link - 1
                            
                            if contador_link == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_link_4_CK = False
                                
                            if contador_link == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_link_3_CK = False

                            if contador_link == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_link_2_CK = False

                            if contador_link == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_link_1_CK = False
                                linkCK = False

                            if contador_link == -1:
                                cont_texto = cont_texto + 4
                                stock_link_1_CK = True
                                stock_link_2_CK = True
                                stock_link_3_CK = True
                                stock_link_4_CK = True
                                linkCK = True
                                contador_link = 4


                        # Samus
                        if mx < 100 and my > 400 and my < 500:
                            contador_samus = contador_samus - 1
                            
                            if contador_samus == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_samus_4_CK = False
                                
                            if contador_samus == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_samus_3_CK = False

                            if contador_samus == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_samus_2_CK = False

                            if contador_samus == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_samus_1_CK = False
                                samusCK = False

                            if contador_samus == -1:
                                cont_texto = cont_texto + 4
                                stock_samus_1_CK = True
                                stock_samus_2_CK = True
                                stock_samus_3_CK = True
                                stock_samus_4_CK = True
                                samusCK = True
                                contador_samus = 4


                        # C. Falcon
                        if mx < 100 and my > 500 and my < 600:
                            contador_falcon = contador_falcon - 1
                            
                            if contador_falcon == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_falcon_4_CK = False
                                
                            if contador_falcon == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_falcon_3_CK = False

                            if contador_falcon == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_falcon_2_CK = False

                            if contador_falcon == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_falcon_1_CK = False
                                falconCK = False

                            if contador_falcon == -1:
                                cont_texto = cont_texto + 4
                                stock_falcon_1_CK = True
                                stock_falcon_2_CK = True
                                stock_falcon_3_CK = True
                                stock_falcon_4_CK = True
                                falconCK = True
                                contador_falcon = 4


                        # Ness
                        if mx > 100 and mx < 200 and my > 0 and my < 100:
                            contador_ness = contador_ness - 1
                            
                            if contador_ness == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_ness_8_CK = False
                                stock_ness_7_CK = True
                                
                            if contador_ness == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_ness_7_CK = False
                                stock_ness_6_CK = True

                            if contador_ness == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_ness_6_CK = False
                                stock_ness_5_CK = True

                            if contador_ness == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_ness_5_CK = False
                                stock_ness_4_CK = True
                                nessCK = False

                            if contador_ness == -1:
                                stock_ness_4_CK = False
                                stock_ness_8_CK = True
                                nessCK = True
                                cont_texto = cont_texto + 4
                                contador_ness = 4


                        # Yoshi
                        if mx > 100 and mx < 200 and my > 100 and my < 200:
                            contador_yoshi = contador_yoshi - 1
                            
                            if contador_yoshi == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_yoshi_4_CK = False
                                
                            if contador_yoshi == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_yoshi_3_CK = False

                            if contador_yoshi == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_yoshi_2_CK = False

                            if contador_yoshi == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_yoshi_1_CK = False
                                yoshiCK = False

                            if contador_yoshi == -1:
                                cont_texto = cont_texto + 4
                                stock_yoshi_1_CK = True
                                stock_yoshi_2_CK = True
                                stock_yoshi_3_CK = True
                                stock_yoshi_4_CK = True
                                yoshiCK = True
                                contador_yoshi = 4


                        # Kirby
                        if mx > 100 and mx < 200 and my > 200 and my < 300:
                            contador_kirby = contador_kirby - 1
                            
                            if contador_kirby == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_kirby_4_CK = False
                                
                            if contador_kirby == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_kirby_3_CK = False

                            if contador_kirby == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_kirby_2_CK = False

                            if contador_kirby == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_kirby_1_CK = False
                                kirbyCK = False

                            if contador_kirby == -1:
                                cont_texto = cont_texto + 4
                                stock_kirby_1_CK = True
                                stock_kirby_2_CK = True
                                stock_kirby_3_CK = True
                                stock_kirby_4_CK = True
                                kirbyCK = True
                                contador_kirby = 4


                        # Fox
                        if mx > 100 and mx < 200 and my > 300 and my < 400:
                            contador_fox = contador_fox - 1
                            
                            if contador_fox == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_fox_4_CK = False
                                
                            if contador_fox == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_fox_3_CK = False

                            if contador_fox == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_fox_2_CK = False

                            if contador_fox == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_fox_1_CK = False
                                foxCK = False

                            if contador_fox == -1:
                                cont_texto = cont_texto + 4
                                stock_fox_1_CK = True
                                stock_fox_2_CK = True
                                stock_fox_3_CK = True
                                stock_fox_4_CK = True
                                foxCK = True
                                contador_fox = 4


                        # Pikachu
                        
                        if mx > 100 and mx < 200 and my > 400 and my < 500:
                            contador_pikachu = contador_pikachu - 1
                                
                            if contador_pikachu == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_pikachu_4_CK = False
                                    
                            if contador_pikachu == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_pikachu_3_CK = False

                            if contador_pikachu == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_pikachu_2_CK = False

                            if contador_pikachu == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_pikachu_1_CK = False
                                pikachuCK = False

                            if contador_pikachu == -1:
                                cont_texto = cont_texto + 4
                                stock_pikachu_1_CK = True
                                stock_pikachu_2_CK = True
                                stock_pikachu_3_CK = True
                                stock_pikachu_4_CK = True
                                pikachuCK = True
                                contador_pikachu = 4


                        # Jigglypuff
                        if mx > 100 and mx < 200 and my > 500 and my < 600:
                            contador_jigglypuff = contador_jigglypuff - 1
                            
                            if contador_jigglypuff == 3:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_jigglypuff_4_CK = False
                                
                            if contador_jigglypuff == 2:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_jigglypuff_3_CK = False

                            if contador_jigglypuff == 1:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_jigglypuff_2_CK = False

                            if contador_jigglypuff == 0:
                                cont_texto = cont_texto - 1
                                textoCK = True
                                stock_jigglypuff_1_CK = False
                                jigglypuffCK = False

                            if contador_jigglypuff == -1:
                                cont_texto = cont_texto + 4
                                stock_jigglypuff_1_CK = True
                                stock_jigglypuff_2_CK = True
                                stock_jigglypuff_3_CK = True
                                stock_jigglypuff_4_CK = True
                                jigglypuffCK = True
                                contador_jigglypuff = 4

                        #--------------------------------------------------------------
                        #--------------------------------------------------------------
                        #--------------------------------------------------------------
                        # Fila 2

                        # Luigi
                        if mx > 600 and mx < 700 and my > 0 and my < 100:
                            contador_luigi_2 = contador_luigi_2 - 1
                            
                            if contador_luigi_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_luigi_4_CK_2 = False
                                

                            if contador_luigi_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_luigi_3_CK_2 = False

                            if contador_luigi_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_luigi_2_CK_2 = False

                            if contador_luigi_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_luigi_1_CK_2 = False
                                luigiCK1 = False

                            if contador_luigi_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_luigi_1_CK_2 = True
                                stock_luigi_2_CK_2 = True
                                stock_luigi_3_CK_2 = True
                                stock_luigi_4_CK_2 = True
                                luigiCK1 = True
                                contador_luigi_2 = 4


                        # Mario
                        if mx > 600 and mx < 700 and my > 100 and my < 200:
                            contador_mario_2 = contador_mario_2 - 1
                            
                            if contador_mario_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_mario_4_CK_2 = False
                                

                            if contador_mario_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_mario_3_CK_2 = False

                            if contador_mario_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_mario_2_CK_2 = False

                            if contador_mario_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_mario_1_CK_2 = False
                                marioCK1 = False

                            if contador_mario_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_mario_1_CK_2 = True
                                stock_mario_2_CK_2 = True
                                stock_mario_3_CK_2 = True
                                stock_mario_4_CK_2 = True
                                marioCK1 = True
                                contador_mario_2 = 4


                        # DK
                        if mx > 600 and mx < 700 and my > 200 and my < 300:
                            contador_dk_2 = contador_dk_2 - 1
                            
                            if contador_dk_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_dk_4_CK_2 = False
                                

                            if contador_dk_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_dk_3_CK_2 = False

                            if contador_dk_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_dk_2_CK_2 = False

                            if contador_dk_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_dk_1_CK_2 = False
                                dkCK1 = False

                            if contador_dk_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_dk_1_CK_2 = True
                                stock_dk_2_CK_2 = True
                                stock_dk_3_CK_2 = True
                                stock_dk_4_CK_2 = True
                                dkCK1 = True
                                contador_dk_2 = 4


                        # Link
                        if mx > 600 and mx < 700 and my > 300 and my < 400:
                            contador_link_2 = contador_link_2 - 1
                            
                            if contador_link_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_link_4_CK_2 = False
                                

                            if contador_link_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_link_3_CK_2 = False

                            if contador_link_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_link_2_CK_2 = False

                            if contador_link_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_link_1_CK_2 = False
                                linkCK1 = False

                            if contador_link_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_link_1_CK_2 = True
                                stock_link_2_CK_2 = True
                                stock_link_3_CK_2 = True
                                stock_link_4_CK_2 = True
                                linkCK1 = True
                                contador_link_2 = 4


                        # Samus
                        if mx > 600 and mx < 700 and my > 400 and my < 500:
                            contador_samus_2 = contador_samus_2 - 1
                            
                            if contador_samus_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_samus_4_CK_2 = False
                                

                            if contador_samus_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_samus_3_CK_2 = False

                            if contador_samus_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_samus_2_CK_2 = False

                            if contador_samus_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_samus_1_CK_2 = False
                                samusCK1 = False

                            if contador_samus_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_samus_1_CK_2 = True
                                stock_samus_2_CK_2 = True
                                stock_samus_3_CK_2 = True
                                stock_samus_4_CK_2 = True
                                samusCK1 = True
                                contador_samus_2 = 4


                        # C. Falcon
                        if mx > 600 and mx < 700 and my > 500 and my < 600:
                            contador_falcon_2 = contador_falcon_2 - 1
                            
                            if contador_falcon_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_falcon_4_CK_2 = False
                                
                            if contador_falcon_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_falcon_3_CK_2 = False

                            if contador_falcon_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_falcon_2_CK_2 = False

                            if contador_falcon_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_falcon_1_CK_2 = False
                                falconCK1 = False

                            if contador_falcon_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_falcon_1_CK_2 = True
                                stock_falcon_2_CK_2 = True
                                stock_falcon_3_CK_2 = True
                                stock_falcon_4_CK_2 = True
                                falconCK1 = True
                                contador_falcon_2 = 4


                        # Ness
                        if mx > 700 and mx < 800 and my > 0 and my < 100:
                            contador_ness_2 = contador_ness_2 - 1
                            
                            if contador_ness_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_ness_8_CK_2 = False
                                stock_ness_7_CK_2 = True
                                
                            if contador_ness_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_ness_7_CK_2 = False
                                stock_ness_6_CK_2 = True

                            if contador_ness_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_ness_6_CK_2 = False
                                stock_ness_5_CK_2 = True

                            if contador_ness_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_ness_5_CK_2 = False
                                stock_ness_4_CK_2 = True
                                nessCK1 = False

                            if contador_ness_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_ness_4_CK_2 = False
                                stock_ness_8_CK_2 = True
                                nessCK1 = True
                                
                                contador_ness_2 = 4


                        # Yoshi
                        if mx > 700 and mx < 800 and my > 100 and my < 200:
                            contador_yoshi_2 = contador_yoshi_2 - 1
                            
                            if contador_yoshi_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_yoshi_4_CK_2 = False
                                
                            if contador_yoshi_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_yoshi_3_CK_2 = False

                            if contador_yoshi_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_yoshi_2_CK_2 = False

                            if contador_yoshi_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_yoshi_1_CK_2 = False
                                yoshiCK1 = False

                            if contador_yoshi_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_yoshi_1_CK_2 = True
                                stock_yoshi_2_CK_2 = True
                                stock_yoshi_3_CK_2 = True
                                stock_yoshi_4_CK_2 = True
                                yoshiCK1 = True
                                contador_yoshi_2 = 4


                        # Kirby
                        if mx > 700 and mx < 800 and my > 200 and my < 300:
                            contador_kirby_2 = contador_kirby_2 - 1
                            
                            if contador_kirby_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_kirby_4_CK_2 = False
                                
                            if contador_kirby_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_kirby_3_CK_2 = False

                            if contador_kirby_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_kirby_2_CK_2 = False

                            if contador_kirby_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_kirby_1_CK_2 = False
                                kirbyCK1 = False

                            if contador_kirby_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_kirby_1_CK_2 = True
                                stock_kirby_2_CK_2 = True
                                stock_kirby_3_CK_2 = True
                                stock_kirby_4_CK_2 = True
                                kirbyCK1 = True
                                contador_kirby_2 = 4


                        # Fox
                        if mx > 700 and mx < 800 and my > 300 and my < 400:
                            contador_fox_2 = contador_fox_2 - 1
                            
                            if contador_fox_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_fox_4_CK_2 = False
                                
                            if contador_fox_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_fox_3_CK_2 = False

                            if contador_fox_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_fox_2_CK_2 = False

                            if contador_fox_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_fox_1_CK_2 = False
                                foxCK1 = False

                            if contador_fox_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_fox_1_CK_2 = True
                                stock_fox_2_CK_2 = True
                                stock_fox_3_CK_2 = True
                                stock_fox_4_CK_2 = True
                                foxCK1 = True
                                contador_fox_2 = 4


                        # Pikachu
                        if mx > 700 and mx < 800 and my > 400 and my < 500:
                            contador_pikachu_2 = contador_pikachu_2 - 1
                            
                            if contador_pikachu_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_pikachu_4_CK_2 = False
                                
                            if contador_pikachu_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_pikachu_3_CK_2 = False

                            if contador_pikachu_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_pikachu_2_CK_2 = False

                            if contador_pikachu_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_pikachu_1_CK_2 = False
                                pikachuCK1 = False

                            if contador_pikachu_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_pikachu_1_CK_2 = True
                                stock_pikachu_2_CK_2 = True
                                stock_pikachu_3_CK_2 = True
                                stock_pikachu_4_CK_2 = True
                                pikachuCK1 = True
                                contador_pikachu_2 = 4


                        # Jigglypuff
                        if mx > 700 and mx < 800 and my > 500 and my < 600:
                            contador_jigglypuff_2 = contador_jigglypuff_2 - 1
                            
                            if contador_jigglypuff_2 == 3:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_jigglypuff_4_CK_2 = False
                                
                            if contador_jigglypuff_2 == 2:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_jigglypuff_3_CK_2 = False

                            if contador_jigglypuff_2 == 1:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_jigglypuff_2_CK_2 = False

                            if contador_jigglypuff_2 == 0:
                                cont_texto2 = cont_texto2 - 1
                                texto2CK = True
                                stock_jigglypuff_1_CK_2 = False
                                jigglypuffCK1 = False

                            if contador_jigglypuff_2 == -1:
                                cont_texto2 = cont_texto2 + 4
                                stock_jigglypuff_1_CK_2 = True
                                stock_jigglypuff_2_CK_2 = True
                                stock_jigglypuff_3_CK_2 = True
                                stock_jigglypuff_4_CK_2 = True
                                jigglypuffCK1 = True
                                contador_jigglypuff_2 = 4
                        
                    

                pygame.display.update()


#---------------------MAIN-----------------------------






opcion_1()

