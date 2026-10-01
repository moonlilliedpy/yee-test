#screen tests
screen remote_community_contents():
    text "Community Platforms" size 65 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    frame:
        style ("ui1_frame" if ui_style == 1 else "ui2_frame")
        xalign 0.5
        hbox:
            imagebutton:
                    idle Transform("gui/presskitsocials/patreon_logo.webp", zoom=0.41)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            imagebutton:
                    idle Transform("gui/presskitsocials/discord_symbol.webp", zoom=0.35)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            imagebutton:
                    idle Transform("gui/presskitsocials/tumblr_logo.webp", zoom=0.43)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            imagebutton:
                    idle Transform("gui/presskitsocials/itchio_logo.webp", zoom=0.43)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            imagebutton:
                    idle Transform("gui/presskitsocials/x_logo.webp", zoom=0.43)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            imagebutton:
                    idle Transform("gui/presskitsocials/tiktok.webp", zoom=0.43)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            imagebutton:
                    idle Transform("gui/presskitsocials/bluesky.webp", zoom=0.43)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            # imagebutton: # STEAM
            #         idle Transform("gui/presskitsocials/bluesky.webp", zoom=0.43)
            #         action OpenURL("https://discord.com/channels/1536169862341333012")
        

    text "Hashtags" size 65 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5#yoffset -30
    text "#DevotionProtocolYou, #DPYGame, #DPYFieldwick" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5#yoffset -45
    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1.png", xzoom=0.9, alpha=0.75)#yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9, alpha=0.75)#yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
###########################################################################################
### EVENTS
###########################################################################################
    text "Events" size 65 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1.png", xzoom=0.9, alpha=0.30, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9, alpha=0.50, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    hbox:
        spacing 20
        xalign 0.5
        text "AU Contest - Until February 28th" size 50 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2")
        imagebutton:
            idle Transform("gui/presskitsocials/x_logo.webp", zoom=0.15)
            action OpenURL("https://discord.com/channels/1536169862341333012")

    #image for contest promo
    text "Share fanart of your own or favorite AU! Three winners will be selected for a prize! Tag your post with #DPYGameContestFebruary and a winner will be selected at the end of the month! Winners will be selected from X and Discord" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5

    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1.png", xzoom=0.9, alpha=0.30, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9, alpha=0.50, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    text "Poll for Q&A - Until February 10th" size 50 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    text "Vote on which patreon submitted questions you want answered in the next stream!" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5


    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1_opaque.webp", xzoom=0.9) #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    null height 10
    text "Found Any Bugs?" size 65 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    null height 10
    text "You can report any bugs, typos or translation errors through the official DP:Y discord server or leave a comment on the itch.io page so it can be fixed as soon as possible!" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    text "Please ensure you're using the latest version of the game before making a report." size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    null height 20
    frame:
        xalign 0.5
        style ("ui1_frame" if ui_style == 1 else "ui2_frame")
        xysize (1200, 150)
        hbox:
            spacing 200
            xalign 0.5
            yalign 0.5
            #text "link to discord" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2")
            imagebutton:
                idle Transform("gui/presskitsocials/discord_word.webp", zoom=0.2)
                action OpenURL("https://discord.com/channels/1536169862341333012/1554191891564593152")
            imagebutton:
                idle Transform("gui/presskitsocials/itchio_word.webp", zoom=0.2)
                action OpenURL("https://dpy.itch.io/dpy/comments?after=0")
    null height 80







screen remote_support_contents():
    text "Follow & Support Development" size 65 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    frame:
        xalign 0.5
        style ("ui1_frame" if ui_style == 1 else "ui2_frame")
        hbox:                        
            imagebutton:
                    idle Transform("gui/presskitsocials/patreon_logo.webp", zoom=0.41)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
            imagebutton:
                    idle Transform("gui/presskitsocials/patreon_word.webp", zoom=0.41)
                    action OpenURL("https://discord.com/channels/1536169862341333012")
                    yalign 0.5
        
    text "If you want to keep up with development, Q&A polls and lore, you can drop into the free tier to sneak a peek of what's going on. We appreciate your support!" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2") xalign 0.5
    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1.png", xzoom=0.9, alpha=0.75) #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9, alpha=0.75) #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
###########################################################################################
### MERCHANDISE
###########################################################################################
    text "Merchandise" size 65 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2")xalign 0.5
    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1.png", xzoom=0.9, alpha=0.30, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9, alpha=0.50, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    
    hbox:
        spacing 20
        xalign 0.5
        text "New Keychain Pre-Order" size 50 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2")
        imagebutton:
            idle Transform("gui/presskitsocials/x_logo.webp", zoom=0.15)
            action OpenURL("https://discord.com/channels/1536169862341333012")
    add Transform("images/temp/squashed.png", zoom=0.3) xalign 0.5
    #image for contest promo
    text "Pre-Orders are available until December 12th!" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2")xalign 0.5

    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1.png", xzoom=0.9, alpha=0.30, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9, alpha=0.50, yzoom=0.4) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    text "All Prints 30% off until November 10th" size 50 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2")xalign 0.5
    add "images/temp/piam.png" xalign 0.5
    text "(Shop link to on sale print listing collection)" size 45 style ("menu_text_ui1" if ui_style == 1 else "menu_text_ui2")xalign 0.5


    if ui_style == 1:
        add Transform("gui/ui1/gamemenubackgroundtitleline_ui1_opaque.webp", xzoom=0.9) #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    else:
        add Transform("gui/ui2/gamemenubackgroundtitleline_ui2.png", xzoom=0.9) xalign -0.406 #yalign -0 at fade_up(0, 155, distance=40, duration=1.0, delay=1)
    null height 80
