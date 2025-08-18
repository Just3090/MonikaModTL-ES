
# by just6889



label android_menu:
    menu:
        "Gifts":
            jump giftmenu
        "Affect":
            jump affectionmenu
        "Changelog":
            jump changelog
        "Just's Notes (porter)":
            jump notas
        # "beta_test":
        #     jump beta_test
        "(BETA - may not work, you need to know the process) Update mod_assets and sprites":
            python:
                mas_generate_custom_sprite_rpys()
            return
        "Nevermind":
            return

label notas:
    # "Problems without solution: NOU sounds and chess game."
    # "I hope this will be fixed on beta 0.4.0."
    # "Really, I spend much time on this."
    "I finally have a custom sprite system working <3"
    "Byeeee!"
    m "Oh maan..."
    return 

label changelog:

    "MAS updated to 0.12.17 and port v1.1"
    "Release 1.1: 'The True Version' - English Edition."
    "Fixed the bug with an incorrect animation when kissing Moni."
    "SFX for NOU also fixed."
    "Chess difficulty improved."
    "Dynamic button to gift spritepacks."
    "Redesign of the custom gift screen."
    "(BETA) Custom sprites are now available. If you don't know how to use them, ask on the Discord server. (Android/data/com.test.mas/files/saves/android/sprites/)"
    "ando also the same mod_assets into 'Android/data/com.test.mas/files/game/'."
    "'custom_bgm' fixed and now works properly. ('Android/data/com.test.mas/files/game/custom_bgm/')" 
    "Update date: 07/10/2025"
    "Port by just6889 (Traduction Club!)"
    "{a=https://traduction-club.live/}{color=#00f}Traduction Club page here{/color}{/a}."
    # "Beta 0.3.7: The Chess Update!!!"
    # "The chess is working yaaaaay"
    # "Actualization date: 05/27/2025"
    # "Port by just6889 | President of Traduction Club (spanish community)"
    # "{a=https://traduction-club.live/}{color=#00f}Traduction Club page here{/color}{/a}."
    # "Beta 0.3.6: Piano Update!!!"
    # "Now the piano works yaaaay"
    # "Actualization date: 04/19/2025"
    # "Port by just6889 | President of Traduction Club (spanish community)"
    # "{a=https://traduction-club.live/}{color=#00f}Traduction Club page here{/color}{/a}."
    # "Beta 0.3.5: Major Update!!!"
    # "Various sprites."
    # "Added button 'Menu Android'."
    # "Added button 'Predefined Gifts'."
    # "Actualization date: 21/03/2025"
    # "Port by just6889"
    return

label affectionmenu:

    "The affection of [persistent._mas_monika_nickname] is [store._mas_getAffection()] points."
    return

label giftmenu:


    menu:
        "Write a Gift":
            call screen give_custom_gift_screen
        "Predefined Gifts":
            call giftmenu_predefined from _call_giftmenu_predefined
        "Dynamic gift menu (All posible sprites)":
            jump giftmenu_dynamic
        "Return":
            return
    return

label giftmenu_dynamic:
    python:
        from store.mas_sprites_json import giftname_map
        import os

        # Ordenar alfabéticamente los nombres de regalo
        sorted_giftnames = sorted([
            giftname for giftname in giftname_map.keys()
            if not giftname.startswith("__")
        ])
        items = [
            (giftname + ".gift", giftname + ".gift", False, False)
            for giftname in sorted_giftnames
        ]
        items.append(("Return", False, False, False))
        display_area = store.mas_ui.SCROLLABLE_MENU_TXT_TALL_AREA
        scroll_align = store.mas_ui.SCROLLABLE_MENU_XALIGN

    $ result = renpy.call_screen("mas_gen_scrollable_menu", items=items, display_area=display_area, scroll_align=scroll_align, nvm_text="Return")

    if result and result != "Return":
        python:
            gift_path = os.path.join(renpy.config.basedir, "characters", result)
            if not os.path.exists(gift_path):
                with open(gift_path, "w") as f:
                    f.write("")
        $ give_custom_gift(result)
    return

init python:
    def get_unregifted_gifts():
        from store.mas_sprites_json import giftname_map
        gifted = list(persistent._mas_filereacts_sprite_gifts.keys())
        return [
            g for g in giftname_map.keys()
            if not g.startswith("__") and g not in gifted
        ]

screen dynamic_gift_menu():
    tag menu
    vbox:
        spacing 10
        for gift in get_unregifted_gifts():
            textbutton gift.replace(".gift", "") action Function(give_custom_gift, gift)
        textbutton "Return" action Return()

default gift_input = ""
init python:
    def give_custom_gift(gift_name):
        """
        Función para dar un regalo personalizado a Monika.
        """
        if gift_name.endswith(".gift") or gift_name.endswith(".txt"):
            filepath = os.path.join(renpy.config.basedir, 'characters', gift_name)
            with open(filepath, "a") as f:
                pass

label giftmenu_predefined:
    
    menu:
        "Ribbon (Bisexual Pride Themed)":
            python:
                gift_input = "bisexualpridethemedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Black and White)":
            python:
                gift_input = "blackandwhiteribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Bronze)":
            python:
                gift_input = "bronzeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Brown)":
            python:
                gift_input = "brownribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gradient)":
            python:
                gift_input = "gradientribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Low-Poly Gradient)":
            python:
                gift_input = "lowpolygradientribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Rainbow Gradient)":
            python:
                gift_input = "rainbowgradientribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (White Polka Dots on Red)":
            python:
                gift_input = "whiteonredpolkadotribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Starry Black Sky)":
            python:
                gift_input = "starryblackskyribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Starry Red Sky)":
            python:
                gift_input = "starryredskyribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Blue and White Stripes)":
            python:
                gift_input = "blueandwhitestripedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pink and White Stripes)":
            python:
                gift_input = "pinkandwhitestripedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Transgender Pride Themed)":
            python:
                gift_input = "transgenderpridethemedribbon.gift"
                give_custom_gift(gift_input)
        "Hairclip (Crescent Moon)":
            python:
                gift_input = "crescentmoonhairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Ghost)":
            python:
                gift_input = "ghosthairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Pumpkin)":
            python:
                gift_input = "pumpkinhairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Bat)":
            python:
                gift_input = "bathairclip.gift"
                give_custom_gift(gift_input)
        "Choker (Chain, Silver)":
            python:
                gift_input = "chokerchainsilver.gift"
                give_custom_gift(gift_input)
        "Choker (Daisy, White)":
            python:
                gift_input = "chokerdaisywhite.gift"
                give_custom_gift(gift_input)
        "Choker (Emerald, Green)":
            python:
                gift_input = "chokeremeraldgreen.gift"
                give_custom_gift(gift_input)
        "Choker (Glitter Bead, Silver)":
            python:
                gift_input = "chokerglitterbeadsilver.gift"
                give_custom_gift(gift_input)
        "Choker (Ribbon, Red)":
            python:
                gift_input = "chokerribbonred.gift"
                give_custom_gift(gift_input)
        "Choker (Ruffles, Red)":
            python:
                gift_input = "chokerrufflesred.gift"
                give_custom_gift(gift_input)
        "Choker (Silk, White)":
            python:
                gift_input = "chokersilkwhite.gift"
                give_custom_gift(gift_input)
        "Choker (Spiked, Star)":
            python:
                gift_input = "chokerspikedstar.gift"
                give_custom_gift(gift_input)
        "Choker (Spiral, Black)":
            python:
                gift_input = "chokerspiralblack.gift"
                give_custom_gift(gift_input)
        "Choker (Thread, Ribbon)":
            python:
                gift_input = "chokerthreadribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Black, mini)":
            python:
                gift_input = "miniblackribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Dark pink, mini)":
            python:
                gift_input = "minidarkpinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gray, mini)":
            python:
                gift_input = "minigrayribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Orange, mini)":
            python:
                gift_input = "miniorangeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pale green, mini)":
            python:
                gift_input = "minipalegreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pink, mini)":
            python:
                gift_input = "minipinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Purple, mini)":
            python:
                gift_input = "minipurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Red, mini)":
            python:
                gift_input = "miniredribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Royal blue, mini)":
            python:
                gift_input = "miniroyalblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Sky blue, mini)":
            python:
                gift_input = "miniskyblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (White, mini)":
            python:
                gift_input = "miniwhiteribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Yellow, mini)":
            python:
                gift_input = "miniyellowribbon.gift"
                give_custom_gift(gift_input)
        "Bralette (Red, Ruffles)":
            python:
                gift_input = "braletteredruffles.gift"
                give_custom_gift(gift_input)
        "Button Up (Flowered)":
            python:
                gift_input = "buttonupflowered.gift"
                give_custom_gift(gift_input)
        "Dress (Dark blue, sparkly)":
            python:
                gift_input = "dressdarkbluesparkle.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Black)":
            python:
                gift_input = "heartcutbikiniblack.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Green)":
            python:
                gift_input = "heartcutbikinigreen.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Pink)":
            python:
                gift_input = "heartcutbikinipink.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Purple)":
            python:
                gift_input = "heartcutbikinipurple.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (White)":
            python:
                gift_input = "heartcutbikiniwhite.gift"
                give_custom_gift(gift_input)
        "Heart-Cut Bikini (Yellow)":
            python:
                gift_input = "heartcutbikiniyellow.gift"
                give_custom_gift(gift_input)
        "Shuchi'in Academy Uniform":
            python:
                gift_input = "shuchiinacademyuniform.gift"
                give_custom_gift(gift_input)
        "Sleeveless Turtleneck (Black)":
            python:
                gift_input = "sleevelessturtleneckblack.gift"
                give_custom_gift(gift_input)
        "T-Shirt (Jurassic Park)":
            python:
                gift_input = "tshirtjurassicpark.gift"
                give_custom_gift(gift_input)
        "T-Shirt (Jurassic World)":
            python:
                gift_input = "tshirtjurassicworld.gift"
                give_custom_gift(gift_input)
        "V-cut Crossed Straps Tanktop (White)":
            python:
                gift_input = "vcutcrossedstrapstanktopwhite.gift"
                give_custom_gift(gift_input)
        "Pearl earrings":
            python:
                gift_input = "pearlearrings.gift"
                give_custom_gift(gift_input)
        "Piercings (Black-silver)":
            python:
                gift_input = "blacksilverpiercings.gift"
                give_custom_gift(gift_input)
        "Dress (Green)":
            python:
                gift_input = "greendress.gift"
                give_custom_gift(gift_input)
        "Jacket (Brown)":
            python:
                gift_input = "brownwinterjacket.gift"
                give_custom_gift(gift_input)
        "Shirt (Put on a happy face)":
            python:
                gift_input = "putonahappyfaceshirt.gift"
                give_custom_gift(gift_input)
        "Shirt (Blue)":
            python:
                gift_input = "blueshirt.gift"
                give_custom_gift(gift_input)
        "Shirt (Rest Here)":
            python:
                gift_input = "resthereshirt.gift"
                give_custom_gift(gift_input)
        "Sweater Vest (Blue)":
            python:
                gift_input = "bluesweatervest.gift"
                give_custom_gift(gift_input)
        "Tanktop (White)": 
            python:
                gift_input = "tanktop.gift"
                give_custom_gift(gift_input)
        "Turtleneck Sweater (Beige)":
            python:
                gift_input = "beigeturtlenecksweater.gift"
                give_custom_gift(gift_input)
        "Hoodie (Green)": 
            python:
                gift_input = "greenhoodie.gift"
                give_custom_gift(gift_input)
        "YoRHa No.2 Type B":
            python:
                gift_input = "2bcosplay.gift"
                give_custom_gift(gift_input)
        "Anchor Necklace":
            python:
                gift_input = "anchor_necklace.gift"
                give_custom_gift(gift_input)
        "Animal Crossing Necklace":
            python:
                gift_input = "animalcrossing_necklace.gift"
                give_custom_gift(gift_input)
        "Cactus Necklace":
            python:
                gift_input = "cactus_necklace.gift"
                give_custom_gift(gift_input)
        "Gold Chain Necklace":
            python:
                gift_input = "goldchain_necklace.gift"
                give_custom_gift(gift_input)
        "Snail Shell Necklace":
            python:
                gift_input = "snailshell_necklace.gift"
                give_custom_gift(gift_input)
        "Purple Star Necklace":
            python:
                gift_input = "star_necklace.gift"
                give_custom_gift(gift_input)
        "Sunflower Necklace":
            python:
                gift_input = "sunflower_necklace.gift"
                give_custom_gift(gift_input)
        "Triforce Necklace":
            python:
                gift_input = "triforce_necklace.gift"
                give_custom_gift(gift_input)
        "Hairclip (Cherry)": 
            python:
                gift_input = "cherryhairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (Heart)": 
            python:
                gift_input = "hearthairclip.gift"
                give_custom_gift(gift_input)
        "Hairclip (8th Note)":
            python:
                gift_input = "musicnotehairclip.gift"
                give_custom_gift(gift_input)
        "Ribbon (Coffee)": 
            python:
                gift_input = "coffeeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gold)": 
            python:
                gift_input = "goldribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Hot Pink)": 
            python:
                gift_input = "hotpinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Lilac)": 
            python:
                gift_input = "lilacribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Lime Green)":
            python:
                gift_input = "limegreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Navy Blue)":
            python:
                gift_input = "navyblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Orange)":
            python:
                gift_input = "orangeribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Royal Purple)":
            python:
                gift_input = "royalpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Sky Blue)": 
            python:
                gift_input = "skyblueribbon.gift"
                give_custom_gift(gift_input)
        "Kimono (Pink)": 
            python:
                gift_input = "pinkkimono.gift"
                give_custom_gift(gift_input)
        "Pullover (Black and White Stripe)":
            python:
                gift_input = "blackandwhitestripedpullover.gift"
                give_custom_gift(gift_input)
        "Bow (Black)": 
            python:
                gift_input = "blackbow.gift"
                give_custom_gift(gift_input)
        "Pullover (Wine Asymmetrical)":
            python:
                gift_input = "wineasymmetricalpullover.gift"
                give_custom_gift(gift_input)
        "Flower (Pink)": 
            python:
                gift_input = "pinkflower.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Blue)":
            python:
                gift_input = "bluetwinribbon.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Green)":
            python:
                gift_input = "greentwinribbon.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Pink)":
            python:
                gift_input = "pinktwinribbon.gift"
                give_custom_gift(gift_input)
        "Twin Ribbon (Yellow)":
            python:
                gift_input = "yellowtwinribbon.gift"
                give_custom_gift(gift_input)
        "Bikini (Shell)": 
            python:
                gift_input = "shellbikini.gift"
                give_custom_gift(gift_input)
        "Hatsune Miku":
            python:
                gift_input = "hatsunemikucosplay.gift"
                give_custom_gift(gift_input)
        "Sakuya Izayoi":
            python:
                gift_input = "sakuyaizayoicosplay.gift"
                give_custom_gift(gift_input)
        "Sweater (Shoulderless)":
            python:
                gift_input = "shoulderlesssweater.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Blue)":
            python:
                gift_input = "8blueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Emerald)":
            python:
                gift_input = "8emeraldribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit White)":
            python:
                gift_input = "8whiteribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Amdek Amber)":
            python:
                gift_input = "amdekamberribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Game Boy Green)":
            python:
                gift_input = "gameboygreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Purple)":
            python:
                gift_input = "8purpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (8-bit Red)":
            python:
                gift_input = "8redribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Super Game Boy Green)":
            python:
                gift_input = "supergameboygreenribbon.gift"
                give_custom_gift(gift_input)
        "Heart Choker":
            python:
                gift_input = "heartchoker.gift"
                give_custom_gift(gift_input)
        "Choker (Flowered)": 
            python:
                gift_input = "floweredchoker.gift"
                give_custom_gift(gift_input)
        "Choker (Simple)": 
            python:
                gift_input = "simplechoker.gift"
                give_custom_gift(gift_input)
        "Bunny Scrunchie (Blue)":
            python:
                gift_input = "bluebunnyscrunchie.gift"
                give_custom_gift(gift_input)
        "Ribbon (Black, s-type)":
            python:
                gift_input = "stypeblackribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Blue, s-type)":
            python:
                gift_input = "stypeblueribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Dark Purple, s-type)":
            python:
                gift_input = "stypedarkpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (White, s-type)":
            python:
                gift_input = "stypedefribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Emerald, s-type)":
            python:
                gift_input = "stypeemeraldribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Gray, s-type)":
            python:
                gift_input = "stypegrayribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Green, s-type)":
            python:
                gift_input = "stypegreenribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Light Purple, s-type)":
            python:
                gift_input = "stypelightpurpleribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Peach, s-type)":
            python:
                gift_input = "stypepeachribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Pink, s-type)":
            python:
                gift_input = "stypepinkribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Platinum, s-type)":
            python:
                gift_input = "stypeplatinumribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Red, s-type)":
            python:
                gift_input = "styperedribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Ruby, s-type)":
            python:
                gift_input = "styperubyribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Sapphire, s-type)":
            python:
                gift_input = "stypesapphireribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Silver, s-type)":
            python:
                gift_input = "stypesilverribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Teal, s-type)":
            python:
                gift_input = "stypetealribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Wine, s-type)":
            python:
                gift_input = "stypewineribbon.gift"
                give_custom_gift(gift_input)
        "Ribbon (Yellow, s-type)":
            python:
                gift_input = "stypeyellowribbon.gift"
                give_custom_gift(gift_input)
        "White and Navy Blue Dress":
            python:
                gift_input = "whiteandnavybluedress.gift"
                give_custom_gift(gift_input)
        "Shirt (Pink)": 
            python:
                gift_input = "pinkshirt.gift"
                give_custom_gift(gift_input)
        "Return":
            return
    return

init python:
    import os
    import shutil

    def copy_log_to_savedir():
        src_dir = os.path.join(renpy.config.basedir, "log")
        dst_dir = renpy.config.savedir

        if os.path.exists(src_dir):
            for fname in os.listdir(src_dir):
                src_file = os.path.join(src_dir, fname)
                dst_file = os.path.join(dst_dir, fname)
                if os.path.isfile(src_file):
                    try:
                        shutil.copy2(src_file, dst_file)
                    except Exception as e:
                        print("Error copiando archivo {} a savedir: {}".format(fname, e))

    config.quit_callbacks.append(copy_log_to_savedir)

init python:
    import os
    import shutil

    def read_debug_txt():
        """
        Busca solo en savedir/androidsaves/debug/debug.txt.
        Si existe, lo lee y lo copia a gamedir/android/debug/debug.txt.
        """
        path2 = os.path.join(renpy.config.savedir, "androidsaves", "debug", "debug.txt")
        path3 = os.path.join(renpy.config.gamedir, "android", "debug", "debug.txt")
        if os.path.exists(path2):
            try:
                with open(path2, "r", encoding="utf-8") as f:
                    content = f.read()
                # Copiar a path3
                dir3 = os.path.dirname(path3)
                if not os.path.exists(dir3):
                    os.makedirs(dir3)
                with open(path3, "w", encoding="utf-8") as f3:
                    f3.write(content)
                return content
            except Exception as e:
                print("Error leyendo o copiando {}: {}".format(path2, e))
        return None

    def read_debug_txt_gamedir():
        """
        Lee el archivo debug.txt desde gamedir/android/debug/debug.txt.
        """
        path3 = os.path.join(renpy.config.gamedir, "android", "debug", "debug.txt")
        if os.path.exists(path3):
            try:
                with open(path3, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                print("Error leyendo {}: {}".format(path3, e))
        return

init -999 python:
    import os
    import json
    import shutil
    import hashlib

    def file_hash(content):
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def mas_generate_custom_sprite_rpys():
        """
        Sincroniza los .json de savedir/android/sprites/mod_assets/monika/j/ con .rpy en gamedir/android/sprites/
        y copia todo mod_assets (excepto .json) a gamedir/android/sprites/mod_assets/
        """
        import fnmatch

        savedir = os.path.join(renpy.config.savedir, "android", "sprites", "mod_assets")
        gamedir = os.path.join(renpy.config.gamedir, "x-android", "x-sprites")
        # Ahora el destino correcto es x-game/x-mod_assets
        gamedir_xgame = os.path.join(renpy.config.gamedir)
        gamedir_mod_assets = os.path.join(gamedir_xgame, "x-mod_assets")
        json_dir = os.path.join(savedir, "monika", "j")

        # Crear gamedir (con prefijo x-) si no existe
        if not os.path.exists(gamedir):
            os.makedirs(gamedir)

        # 1. Buscar todos los .json en savedir/android/sprites/mod_assets/monika/j/
        json_files = []
        if os.path.exists(json_dir):
            json_files = sorted([f for f in os.listdir(json_dir) if f.endswith(".json")])


        # 2. Limpiar .rpy huérfanos (ahora con prefijo 'x-')
        rpy_files = sorted([f for f in os.listdir(gamedir) if f.endswith(".rpy") and (f.startswith("x-infoj_") or f.startswith("x-dict_"))])
        for rpy in rpy_files:
            base = rpy.replace(".rpy", "")
            # El nombre json esperado
            if base.startswith("x-infoj_"):
                json_name = base[7:]  # quitar 'x-infoj_'
            elif base.startswith("x-dict_"):
                json_name = base[7:]
            else:
                continue
            if (json_name + ".json") not in json_files:
                # Eliminar .rpy
                os.remove(os.path.join(gamedir, rpy))
                # Eliminar .rpyc si existe
                rpyc = os.path.join(gamedir, base + ".rpyc")
                if os.path.exists(rpyc):
                    os.remove(rpyc)
                # Eliminar .hash si existe
                hashfile = os.path.join(gamedir, rpy + ".hash")
                if os.path.exists(hashfile):
                    os.remove(hashfile)

        # 3. Generar .rpy para cada .json (con prefijo 'x-')
        id_base = 154
        changes = False
        for idx, json_name in enumerate(json_files):
            json_path = os.path.join(json_dir, json_name)
            with open(json_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except Exception as e:
                    print("Error leyendo {}: {}".format(json_name, e))
                    continue

            # 1. Archivo infoj
            json_str = json.dumps(data, ensure_ascii=False, indent=4)
            json_str = json_str.replace(': true', ': True').replace(': false', ': False')
            infoj_content = (
                'init -20 python in mas_sprites_json:\n'
                '    infoj.insert(0, %s)\n' % json_str
            )
            infoj_rpy = os.path.join(gamedir, "x-infoj_" + json_name.replace('.json','') + ".rpy")
            infoj_rpyc = os.path.join(gamedir, "x-infoj_" + json_name.replace('.json','') + ".rpyc")
            infoj_hashfile = infoj_rpy + ".hash"
            infoj_hash = file_hash(infoj_content)
            prev_infoj_hash = None
            if os.path.exists(infoj_hashfile):
                with open(infoj_hashfile, "r") as f:
                    prev_infoj_hash = f.read().strip()
            if infoj_hash != prev_infoj_hash:
                with open(infoj_rpy, "w", encoding="utf-8") as f:
                    f.write(infoj_content)
                with open(infoj_hashfile, "w") as f:
                    f.write(infoj_hash)
                if os.path.exists(infoj_rpyc):
                    os.remove(infoj_rpyc)
                changes = True

            # 2. Archivo dict_
            dict_content = (
                'init 190 python in mas_sprites_json:\n'
                '    addSpriteObject(infoj[%d])\n' % (id_base+idx)
            )
            dict_rpy = os.path.join(gamedir, "x-dict_" + json_name.replace('.json','') + ".rpy")
            dict_rpyc = os.path.join(gamedir, "x-dict_" + json_name.replace('.json','') + ".rpyc")
            dict_hashfile = dict_rpy + ".hash"
            dict_hash = file_hash(dict_content)
            prev_dict_hash = None
            if os.path.exists(dict_hashfile):
                with open(dict_hashfile, "r") as f:
                    prev_dict_hash = f.read().strip()
            if dict_hash != prev_dict_hash:
                with open(dict_rpy, "w", encoding="utf-8") as f:
                    f.write(dict_content)
                with open(dict_hashfile, "w") as f:
                    f.write(dict_hash)
                if os.path.exists(dict_rpyc):
                    os.remove(dict_rpyc)
                changes = True

        # 4. Copiar mod_assets (excepto .json) a x-game/x-mod_assets/ y renombrar con prefijo 'x-'
        def copytree_nojson_xprefix(src, dst):
            # Prefijar solo en el destino, no modificar dirs
            for root, dirs, files in os.walk(src):
                rel = os.path.relpath(root, src)
                if rel == ".":
                    dst_root = dst
                else:
                    rel_parts = rel.split(os.sep)
                    rel_x = ["x-" + part for part in rel_parts]
                    dst_root = os.path.join(dst, *rel_x)
                if not os.path.exists(dst_root):
                    os.makedirs(dst_root)
                for file in files:
                    if not file.endswith(".json"):
                        src_file = os.path.join(root, file)
                        dst_file = os.path.join(dst_root, "x-" + file)
                        shutil.copy2(src_file, dst_file)
        if os.path.exists(savedir):
            copytree_nojson_xprefix(savedir, gamedir_mod_assets)

        if changes:
            renpy.call_in_new_context("mas_custom_sprites_confirm_restart")

label mas_custom_sprites_confirm_restart:
    $ result = renpy.call_screen(
        "dialog",
        message=_("Custom sprites updated.\nA restart is required to apply\nthese changes."),
        ok_action=Return()
    )
    return

init -1000 python:
    import os
    import shutil

    def ensure_android_sprites_savedir():
        sprites_dir = os.path.join(renpy.config.savedir, "android", "sprites")
        if not os.path.exists(sprites_dir):
            os.makedirs(sprites_dir)
        marker_file = os.path.join(sprites_dir, "put-mod_assets-here.txt")
        if not os.path.exists(marker_file):
            with open(marker_file, "w", encoding="utf-8") as f:
                f.write("Place your mod_assets folders here for custom sprites.\n")

    def ensure_android_gifts_savedir():
        gifts_dir = os.path.join(renpy.config.savedir, "android", "gifts")
        if not os.path.exists(gifts_dir):
            os.makedirs(gifts_dir)
        marker_file = os.path.join(gifts_dir, "put_your_gifts_here-but-this-dont-work-yet_sorry.txt")
        if not os.path.exists(marker_file):
            with open(marker_file, "w", encoding="utf-8") as f:
                f.write("Place your custom gift files here.\n")
        characters_dir = os.path.join(renpy.config.basedir, "characters")
        for fname in os.listdir(gifts_dir):
            if fname == "put_your_gifts_here-but-this-dont-work-yet_sorry.txt":
                continue
            src_file = os.path.join(gifts_dir, fname)
            dst_file = os.path.join(characters_dir, fname)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)

default persistent.language = None

screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label _("Please select a language"):
                style "confirm_prompt"
                xalign 0.5

            vbox:
                style_prefix "radio"
                label _("Language")

                # Real languages should go in alphabetical order by English name.
                textbutton "English" text_font "gui/font/Aller_Rg.ttf" action [
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Quit())
                ]
                # textbutton "한국어" text_font "gui/font/NotoSansKR-Regular.ttf" action [
                #     Language("ko"),
                #     SetField(persistent, "language", "ko"),
                #     SetScreenVariable("chosen_lang", "ko"),
                #     Show("dialog", message="변경 사항을 적용하려면 게임을 재시작하는 것이 좋습니다.", ok_action=Quit())
                # ]
                # textbutton "中文" text_font "gui/font/NotoSansSC-Regular.ttf" action [
                #     Language("zh_CN"),
                #     SetField(persistent, "language", "zh_CN"),
                #     SetScreenVariable("chosen_lang", "zh_CN"),
                #     Show("dialog", message="변경 사항을 적용하려면 게임을 재시작하는 것이 좋습니다.", ok_action=Quit())
                # ]
                textbutton "Español" text_font "gui/font/Aller_Rg.ttf" action [
                    SetField(persistent, "language", "spanish"),
                    SetScreenVariable("chosen_lang", "spanish"),
                    Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Quit())
                ]
                # textbutton "Français" text_font "gui/font/Metropolis-Regular.otf" action [
                #     Language("fr"),
                #     SetField(persistent, "language", "fr"),
                #     SetScreenVariable("chosen_lang", "fr"),
                #     Show("dialog", message="Il est recommandé de redémarrer le jeu pour appliquer les changements.", ok_action=Quit())
                # ]
                # textbutton "日本語" text_font "gui/font/NotoSansJP-Regular.ttf" action [
                #     Language("ja"),
                #     SetField(persistent, "language", "ja"),
                #     SetScreenVariable("chosen_lang", "ja"),
                #     Show("dialog", message="変更を適用するにはゲームを再起動することをおすすめします。", ok_action=Quit())
                # ]
                # textbutton "Português (BR)" text_font "gui/font/Metropolis-Regular.otf" action [
                #     Language("pt_BR"),
                #     SetField(persistent, "language", "pt_BR"),
                #     SetScreenVariable("chosen_lang", "pt_BR"),
                #     Show("dialog", message="É recomendado reiniciar o jogo para aplicar as alterações.", ok_action=Quit())
                # ]
                # textbutton "Español (MX)" text_font "DejaVuSans.ttf" action [
                #     Language("spanish_mx"),
                #     SetField(persistent, "language", "spanish_mxF"),
                #     SetScreenVariable("chosen_lang", "spanish_mx"),
                #     Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Quit())
                # ]
                # textbutton "Português (BR)" text_font "DejaVuSans.ttf" action [
                #     Language("ptBR"),
                #     SetField(persistent, "language", "ptBR"),
                #     SetScreenVariable("chosen_lang", "ptBR"),
                #     Show("dialog", message="Recomenda-se reiniciar para aplicar as alterações.", ok_action=Quit())
                # ]

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Quit())
                    ] style "ok_button_custom"

# Define el estilo personalizado para el botón "OK"
style ok_button_custom is button:
    background None  # Sin fondo
    foreground None  # Sin borde o efecto de selección
    hover_background None  # Sin efecto al pasar el mouse
    hover_foreground None  # Sin borde al pasar el mouse
    insensitive_background None  # Sin efecto cuando está deshabilitado
    insensitive_foreground None

label choose_language:
    call screen choose_language
    return