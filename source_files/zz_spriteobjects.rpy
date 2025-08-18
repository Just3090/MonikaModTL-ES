














init -2 python in mas_sprites:



    import store

    temp_storage = dict()








    _hair__testing_entry = False
    _hair__testing_exit = False
    _clothes__testing_entry = False
    _clothes__testing_exit = False
    _acs__testing_entry = False
    _acs__testing_exit = False





    def _acs_wear_if_found(_moni_chr, acs_name):
        """
        Wears the acs if the acs exists

        IN:
            _moni_chr - MASMonika object
            acs_name - name of the accessory
        """
        acs_to_wear = store.mas_sprites.get_sprite(
            store.mas_sprites.SP_ACS,
            acs_name
        )
        if acs_to_wear is not None:
            _moni_chr.wear_acs(acs_to_wear)


    def _acs_wear_if_gifted(_moni_chr, acs_name):
        """
        Wears the acs if it exists and has been gifted/reacted.
        It has been gifted/reacted if the selectable is unlocked.

        IN:
            _moni_chr - MASMonika object
            acs_name - name of the accessory
        """
        acs_to_wear = store.mas_sprites.get_sprite(
            store.mas_sprites.SP_ACS,
            acs_name
        )
        if acs_to_wear is not None and store.mas_SELisUnlocked(acs_to_wear):
            _moni_chr.wear_acs(acs_to_wear)


    def _acs_wear_if_in_tempstorage(_moni_chr, key):
        """
        Wears the acs in tempstorage at the given key, if any.

        IN:
            _moni_chr - MASMonika object
            key - key in tempstorage
        """
        acs_items = temp_storage.get(key, None)
        if acs_items is not None:
            for acs_item in acs_items:
                _moni_chr.wear_acs(acs_item)


    def _acs_wear_if_in_tempstorage_s(_moni_chr, key):
        """
        Wears a single acs in tempstorage at the given key, if any.

        IN:
            _moni_chr - MASMonika object
            key - key in tempstorage
        """
        acs_item = temp_storage.get(key, None)
        if acs_item is not None:
            _moni_chr.wear_acs(acs_item)


    def _acs_wear_if_wearing_acs(_moni_chr, acs, acs_to_wear):
        """
        Wears the given acs if wearing another acs.

        IN:
            _moni_chr - MASMonika object
            acs - acs to check if wearing
            acs_to_wear - acs to wear if wearing acs
        """
        if _moni_chr.is_wearing_acs(acs):
            _moni_chr.wear_acs(acs_to_wear)


    def _acs_wear_if_wearing_type(_moni_chr, acs_type, acs_to_wear):
        """
        Wears the given acs if wearing an acs of the given type.

        IN:
            _moni_chr - MASMonika object
            acs_type - acs type to check if wearing
            acs_to_wear - acs to wear if wearing acs type
        """
        if _moni_chr.is_wearing_acs_type(acs_type):
            _moni_chr.wear_acs(acs_to_wear)


    def _acs_wear_if_not_wearing_type(_moni_chr, acs_type, acs_to_wear):
        """
        Wears the given acs if NOT wearing an acs of the given type.

        IN:
            _moni_chr - MASMonika object
            acs_type - asc type to check if not wearing
            acs_to_wear - acs to wear if not wearing acs type
        """
        if not _moni_chr.is_wearing_acs_type(acs_type):
            _moni_chr.wear_acs(acs_to_wear)


    def _acs_remove_if_found(_moni_chr, acs_name):
        """
        REmoves an acs if the name exists

        IN:
            _moni_chr - MASMonika object
            acs_name - name of the accessory to remove
        """
        acs_to_remove = store.mas_sprites.get_sprite(
            store.mas_sprites.SP_ACS,
            acs_name
        )
        if acs_to_remove is not None:
            _moni_chr.remove_acs(acs_to_remove)


    def _acs_ribbon_save_and_remove(_moni_chr):
        """
        Removes ribbon acs and aves them to temp storage.

        IN:
            _moni_chr - MASMonika object
        """
        prev_ribbon = _moni_chr.get_acs_of_type("ribbon")
        
        
        if prev_ribbon != store.mas_acs_ribbon_blank:
            temp_storage["hair.ribbon"] = prev_ribbon
        
        if prev_ribbon is not None:
            _moni_chr.remove_acs(prev_ribbon)
        
        
        store.mas_lockEVL("monika_ribbon_select", "EVE")


    def _acs_ribbon_like_save_and_remove(_moni_chr):
        """
        Removes ribbon-like acs and saves them to temp storage, if found

        IN:
            _moni_chr - MASMonika object
        """
        prev_ribbon_like = _moni_chr.get_acs_of_exprop("ribbon-like")
        
        if prev_ribbon_like is not None:
            _moni_chr.remove_acs(prev_ribbon_like)
            temp_storage["hair.ribbon"] = prev_ribbon_like


    def _acs_save_and_remove_exprop(_moni_chr, exprop, key, lock_topics):
        """
        Removes acs with given exprop, saving them to temp storage with
        given key.
        Also locks topics with the exprop if desired

        IN:
            _moni_chr - MASMonika object
            exprop - exprop to remove and save acs
            key - key to use for temp storage
            lock_topics - True will lock topics associated with this exprop
                False will not
        """
        acs_items = _moni_chr.get_acs_of_exprop(exprop, get_all=True)
        if len(acs_items) > 0:
            temp_storage[key] = acs_items
            _moni_chr.remove_acs_exprop(exprop)
        
        if lock_topics:
            lock_exprop_topics(exprop)


    def _hair_unlock_select_if_needed():
        """
        Unlocks the hairdown selector if enough hair is unlocked.
        """
        if len(store.mas_selspr.filter_hair(True)) > 1:
            store.mas_unlockEVL("monika_hair_select", "EVE")


    def _clothes_baked_entry(_moni_chr):
        """
        Clothes baked entry
        """
        for prompt_key in store.mas_selspr.PROMPT_MAP:
            if prompt_key != "clothes":
                prompt_ev = store.mas_selspr.PROMPT_MAP[prompt_key].get(
                    "_ev",
                    None
                )
                if prompt_ev is not None:
                    store.mas_lockEVL(prompt_ev, "EVE")
        
        
        _moni_chr.remove_all_acs()
        
        store.mas_selspr._switch_to_wear_prompts()









    def _hair_def_entry(_moni_chr, **kwargs):
        """
        Entry programming point for ponytail
        """
        pass

    def _hair_def_exit(_moni_chr, **kwargs):
        """
        Exit programming point for ponytail
        """
        pass

    def _hair_down_entry(_moni_chr, **kwargs):
        """
        Entry programming point for hair down
        """
        pass

    def _hair_down_exit(_moni_chr, **kwargs):
        """
        Exit programming point for hair down
        """
        pass

    def _hair_bun_entry(_moni_chr, **kwargs):
        """
        Entry programming point for hair bun
        """
        pass

    def _hair_orcaramelo_bunbraid_exit(_moni_chr, **kwargs):
        """
        Exit prog point for bunbraid
        """
        
        _acs_remove_if_found(_moni_chr, "orcaramelo_sakuya_izayoi_headband")

    def _hair_braided_entry(_moni_chr, **kwargs):
        """
        Entry prog point for braided hair
        """
        _moni_chr.wear_acs(store.mas_acs_rin_bows_back)
        _moni_chr.wear_acs(store.mas_acs_rin_bows_front)

    def _hair_braided_exit(_moni_chr, **kwargs):
        """
        Exit prog point for braided hair
        """
        _moni_chr.remove_acs(store.mas_acs_rin_bows_front)
        _moni_chr.remove_acs(store.mas_acs_rin_bows_back)
        
        _moni_chr.remove_acs(store.mas_acs_rin_ears)

    def _hair_wet_entry(_moni_chr, **kwargs):
        """
        Entry prog point for wet hair
        """
        
        
        _moni_chr._set_ahoge(None)








    def _clothes_def_entry(_moni_chr, **kwargs):
        """
        Entry programming point for def clothes
        """
        store.mas_lockEVL("mas_compliment_outfit", "CMP")





    def _clothes_def_exit(_moni_chr, **kwargs):
        """
        Exit programming point for def clothes
        """
        
        store.mas_unlockEVL("mas_compliment_outfit", "CMP")


    def _clothes_rin_exit(_moni_chr, **kwargs):
        """
        Exit programming point for rin clothes
        """
        _moni_chr.remove_acs(store.mas_acs_rin_ears)


    def _clothes_marisa_exit(_moni_chr, **kwargs):
        """
        Exit programming point for marisa clothes
        """
        _moni_chr.remove_acs(store.mas_acs_marisa_strandbow)


    def _clothes_orcaramelo_hatsune_miku_entry(_moni_chr, **kwargs):
        """
        Entry pp for orcaramelo miku
        """
        outfit_mode = kwargs.get("outfit_mode", False)
        
        if outfit_mode:
            
            twintails = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_HAIR,
                "orcaramelo_twintails"
            )
            if twintails is not None:
                _moni_chr.change_hair(twintails)
                
                
                _acs_wear_if_found(
                    _moni_chr,
                    "orcaramelo_hatsune_miku_headset"
                )
                _acs_wear_if_found(
                    _moni_chr,
                    "orcaramelo_hatsune_miku_twinsquares"
                )


    def _clothes_orcaramelo_hatsune_miku_exit(_moni_chr, **kwargs):
        """
        Exit pp for orcaramelo miku
        """
        
        _acs_remove_if_found(
            _moni_chr,
            "orcaramelo_hatsune_miku_headset"
        )
        _acs_remove_if_found(
            _moni_chr,
            "orcaramelo_hatsune_miku_twinsquares"
        )


    def _clothes_orcaramelo_sakuya_izayoi_entry(_moni_chr, **kwargs):
        """
        Entry pp for orcaramelo sakuya
        """
        outfit_mode = kwargs.get("outfit_mode", False)
        
        if outfit_mode:
            
            bunbraid = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_HAIR,
                "orcaramelo_bunbraid"
            )
            if bunbraid is not None:
                _moni_chr.change_hair(bunbraid)
                
                
                _acs_wear_if_found(
                    _moni_chr,
                    "orcaramelo_sakuya_izayoi_headband"
                )
                _acs_wear_if_found(
                    _moni_chr,
                    "orcaramelo_sakuya_izayoi_strandbow"
                )
                
                
                ribbon_acs = _moni_chr.get_acs_of_type("ribbon")
                if ribbon_acs is not None:
                    _moni_chr.remove_acs(ribbon_acs)


    def _clothes_orcaramelo_sakuya_izayoi_exit(_moni_chr, **kwargs):
        """
        Exit pp for orcaramelo sakuya
        """
        
        _acs_remove_if_found(
            _moni_chr,
            "orcaramelo_sakuya_izayoi_headband"
        )
        _acs_remove_if_found(
            _moni_chr,
            "orcaramelo_sakuya_izayoi_strandbow"
        )


    def _clothes_dress_newyears_entry(_moni_chr, **kwargs):
        """
        entry progpoint for dress_newyears
        """
        outfit_mode = kwargs.get("outfit_mode", False)
        
        if outfit_mode:
            
            
            hairclip = _moni_chr.get_acs_of_type("left-hair-clip")
            if hairclip:
                _moni_chr.remove_acs(hairclip)
            
            
            ribbon = _moni_chr.get_acs_of_type("ribbon")
            if ribbon:
                _moni_chr.remove_acs(ribbon)


    def _clothes_dress_newyears_exit(_moni_chr, **kwargs):
        """
        exit progpoint for dress_newyears
        """
        _moni_chr.remove_acs(store.mas_acs_flower_crown)
        _moni_chr.remove_acs(store.mas_acs_hairties_bracelet_brown)


    def _clothes_sundress_white_exit(_moni_chr, **kwargs):
        """
        Exit programming point for sundress white
        """
        
        
        _moni_chr.remove_acs(store.mas_acs_hairties_bracelet_brown)


    def _clothes_velius94_dress_whitenavyblue_entry(_moni_chr, **kwargs):
        """
        Entry prog point for navyblue dress
        """
        outfit_mode = kwargs.get("outfit_mode", False)
        
        if outfit_mode:
            
            if (
                    not _moni_chr.is_wearing_hair_with_exprop("ribbon")
                    or _moni_chr.is_wearing_hair_with_exprop("twintails")
            ):
                _moni_chr.change_hair(store.mas_hair_def)
            
            _acs_wear_if_gifted(_moni_chr, "velius94_bunnyscrunchie_blue")

    def _clothes_bath_towel_white_entry(_moni_chr, **kwargs):
        """
        Entry prog point for bath towel
        """
        outfit_mode = kwargs.get("outfit_mode", False)
        
        if outfit_mode:
            _moni_chr.change_hair(store.mas_hair_wet, by_user=False)
        
        _moni_chr.wear_acs(store.mas_acs_water_drops)

    def _clothes_bath_towel_white_exit(_moni_chr, **kwargs):
        """
        Exit prog point for bath towel
        """
        
        _moni_chr.remove_acs(store.mas_acs_water_drops)

    def _clothes_briaryoung_shuchiin_academy_uniform_entry(_moni_chr, **kwargs):
        """
        Entry prog point for the shuchiin academy uniform
        """
        
        
        outfit_mode = kwargs.get("outfit_mode", False)
        
        if outfit_mode:
            
            straight_bangs = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_HAIR,
                "briaryoung_down_straight_bangs"
            )
            if straight_bangs is not None:
                _moni_chr.change_hair(straight_bangs)
                
                
                _acs_wear_if_found(_moni_chr, "briaryoung_front_bow_black")

    def _clothes_briaryoung_shuchiin_academy_uniform_exit(_moni_chr, **kwargs):
        """
        Exit prog point for the shuchiin academy uniform
        """
        
        _acs_remove_if_found(_moni_chr, "briaryoung_front_bow_black")

    def _clothes_hatana_2b_entry(_moni_chr, **kwargs):
        """
        Entry pp for hatana 2b
        """
        outfit_mode = kwargs.get("outfit_mode", False)
        
        if outfit_mode:
            
            downshort = store.mas_sprites.get_sprite(
                store.mas_sprites.SP_HAIR,
                "echo_downshort"
            )
            _moni_chr.change_hair(downshort if downshort is not None else store.mas_hair_down)
        
        
        _acs_remove_if_found(_moni_chr, "promisering")


    def _clothes_hatana_2b_exit(_moni_chr, **kwargs):
        """
        Exit prog point for hatana 2b
        """
        
        if store.persistent._mas_acs_enable_promisering:
            _moni_chr.wear_acs(store.mas_acs_promisering)






    def _acs_quetzalplushie_entry(_moni_chr, **kwargs):
        """
        Entry programming point for quetzal plushie acs
        """
        
        store.mas_showEVL('monika_plushie', 'EVE', _random=True)
        
        if store.persistent._mas_d25_deco_active:
            _moni_chr.wear_acs(store.mas_acs_quetzalplushie_santahat)

    def _acs_quetzalplushie_exit(_moni_chr, **kwargs):
        """
        Exit programming point for quetzal plushie acs
        """
        
        store.mas_hideEVL('monika_plushie', 'EVE', derandom=True)
        
        
        _moni_chr.remove_acs(store.mas_acs_quetzalplushie_santahat)
        
        _moni_chr.remove_acs(store.mas_acs_quetzalplushie_antlers)

    def _acs_center_quetzalplushie_entry(_moni_chr, **kwargs):
        """
        Entry programming point for quetzal plushie (mid version) acs
        """
        store.mas_showEVL("monika_plushie", "EVE", _random=True)
        
        if store.persistent._mas_d25_deco_active:
            _moni_chr.wear_acs(store.mas_acs_quetzalplushie_center_santahat)

    def _acs_center_quetzalplushie_exit(_moni_chr, **kwargs):
        """
        Exit programming point for quetzal plushie (mid version) acs
        """
        store.mas_hideEVL("monika_plushie", "EVE", derandom=True)
        
        _moni_chr.remove_acs(store.mas_acs_quetzalplushie_center_santahat)



    def _acs_quetzalplushie_santahat_entry(_moni_chr, **kwargs):
        """
        Entry programming point for quetzal plushie santa hat acs
        """
        
        _moni_chr.wear_acs(store.mas_acs_quetzalplushie)

    def _acs_center_quetzalplushie_santahat_entry(_moni_chr, **kwargs):
        """
        Entry programming point for quetzal plushie santa hat (mid version) acs
        """
        _moni_chr.wear_acs(store.mas_acs_center_quetzalplushie)

    def _acs_quetzalplushie_antlers_entry(_moni_chr, **kwargs):
        """
        Entry programming point for quetzal plushie antlers acs
        """
        
        _moni_chr.wear_acs(store.mas_acs_quetzalplushie)

    def _acs_heartchoc_entry(_moni_chr, **kwargs):
        """
        Entry programming point for heartchoc acs
        """
        
        
        
        
        
        
        if not (store.mas_isF14() or store.mas_isD25Season()):
            if _moni_chr.is_wearing_acs(store.mas_acs_quetzalplushie):
                _moni_chr.wear_acs(store.mas_acs_center_quetzalplushie)
        
        else:
            _moni_chr.remove_acs(store.mas_acs_quetzalplushie)

    def _acs_heartchoc_exit(_moni_chr, **kwargs):
        """
        Exit programming point for heartchoc acs
        """
        if _moni_chr.is_wearing_acs(store.mas_acs_center_quetzalplushie):
            _moni_chr.wear_acs(store.mas_acs_quetzalplushie)

init -1 python:








































    mas_hair_def = MASHair(
        "def",
        "def",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),


        ex_props={
            "ribbon": True,
            "ribbon-restore": True
        }
    )
    store.mas_sprites.init_hair(mas_hair_def)
    store.mas_selspr.init_selectable_hair(
        mas_hair_def,
        "Ponytail",
        "def",
        "hair",
        select_dlg=[
            _("Do you like my ponytail, [player]?")
        ]
    )
    store.mas_selspr.unlock_hair(mas_hair_def)





    mas_hair_down = MASHair(
        "down",
        "down",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        ex_props={
            store.mas_sprites.EXP_H_NT: True,
        }



    )
    store.mas_sprites.init_hair(mas_hair_down)
    store.mas_selspr.init_selectable_hair(
        mas_hair_down,
        "Down",
        "down",
        "hair",
        select_dlg=[
            (_("Feels nice to let my hair down..."))
        ]
    )





    mas_hair_downtiedstrand = MASHair(
        "downtiedstrand",
        "downtiedstrand",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        ex_props={
            store.mas_sprites.EXP_H_RQCP: store.mas_sprites.EXP_C_C_DTS,
            store.mas_sprites.EXP_H_TS: True,
            store.mas_sprites.EXP_H_NT: True,
        }
    )
    store.mas_sprites.init_hair(mas_hair_downtiedstrand)
    store.mas_selspr.init_selectable_hair(
        mas_hair_downtiedstrand,
        "Down (Tied strand)",
        "downtiedstrand",
        "hair",
        select_dlg=[
            _("Feels nice to let my hair down..."),
            _("Looks cute, don't you think?")
        ]
    )





    mas_hair_braided = MASHair(
        "braided",
        "braided",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        ex_props={
            store.mas_sprites.EXP_H_TB: True,
            store.mas_sprites.EXP_H_RQCP: "rin"
        },
        entry_pp=store.mas_sprites._hair_braided_entry,
        exit_pp=store.mas_sprites._hair_braided_exit
    )
    store.mas_sprites.init_hair(mas_hair_braided)
    store.mas_selspr.init_selectable_hair(
        mas_hair_braided,
        "Braided",
        "braided",
        "hair",
        select_dlg=[
            _("Looks cute, don't you think?")
        ]
    )





    mas_hair_wet = MASHair(
        "wet",
        "wet",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        ex_props={
            store.mas_sprites.EXP_H_RQCP: [store.mas_sprites.EXP_C_WET, store.mas_sprites.EXP_C_BRS],
            store.mas_sprites.EXP_H_NT: True,
            store.mas_sprites.EXP_H_WET: True
        },
        entry_pp=store.mas_sprites._hair_wet_entry
    )
    store.mas_sprites.init_hair(mas_hair_wet)





    mas_hair_custom = MASHair(
        "custom",
        "custom",
        MASPoseMap(),

        
        split=MASPoseMap(
            default=False,
            use_reg_for_l=True
        ),
    )
    store.mas_sprites.init_hair(mas_hair_custom)


init -1 python:
































    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_bent",
        "ahoge_bent",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_curl",
        "ahoge_curl",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_double",
        "ahoge_double",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_heart",
        "ahoge_heart",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_lightning",
        "ahoge_lightning",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_sharp",
        "ahoge_sharp",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_simple",
        "ahoge_simple",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_small",
        "ahoge_small",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))







    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_swoop",
        "ahoge_swoop",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=13,
    ))





    store.mas_sprites.init_acs(MASAccessory(
        "ahoge_twisty",
        "ahoge_twisty",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ahoge",
        rec_layer=MASMonika.AFH_ACS,
        priority=7,
    ))





    mas_acs_candycane = MASAccessory(
        "candycane",
        "candycane",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=True,
        acs_type="plate",
        mux_type=store.mas_sprites.DEF_MUX_LD,
        keep_on_desk=False
    )
    store.mas_sprites.init_acs(mas_acs_candycane)





    mas_acs_christmascookies = MASAccessory(
        "christmas_cookies",
        "christmas_cookies",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=True,
        acs_type="plate",
        mux_type=store.mas_sprites.DEF_MUX_LD,
        keep_on_desk=False
    )
    store.mas_sprites.init_acs(mas_acs_christmascookies)





    mas_acs_mug = MASAccessory(
        "mug",
        "mug",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=True,
        acs_type="mug",
        mux_type=["mug"],
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_mug)





    mas_acs_thermos_mug = MASAccessory(
        "thermos_mug",
        "thermos_mug",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=True,
        acs_type="thermos-mug"
    )
    store.mas_sprites.init_acs(mas_acs_thermos_mug)
    store.mas_selspr.init_selectable_acs(
        mas_acs_thermos_mug,
        "Thermos (Just Monika)",
        "thermos_justmonika",
        "thermos-mug"
    )





    mas_acs_ear_rose = MASAccessory(
        "ear_rose",
        "ear_rose",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        acs_type="left-hair-flower-ear",
        mux_type=[
            "left-hair-flower-ear",
            "left-hair-flower"
        ],
        ex_props={
            "left-hair-strand-eye-level": True,
        },
        priority=20,
        stay_on_start=False,
        rec_layer=MASMonika.PST_ACS,
    )
    store.mas_sprites.init_acs(mas_acs_ear_rose)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ear_rose,
        "Rose",
        "hairflower_rose",
        "left-hair-flower",
        hover_dlg=[
            _("TALE AS OLD AS TIME"),
        ],
        select_dlg=[
            _("TRUE AS IT CAN BE"),
        ]
    )





    mas_acs_hairties_bracelet_brown = MASSplitAccessory(
        "hairties_bracelet_brown",
        "hairties_bracelet_brown",
        MASPoseMap(
            p1="1",
            p2="2",
            p3="1",
            p4="4",
            p5="5",
            p6=None,
            p7="1"
        ),
        stay_on_start=True,
        acs_type="wrist-bracelet",
        mux_type=["wrist-bracelet"],
        ex_props={
            "bare wrist": True,
        },
        rec_layer=MASMonika.ASE_ACS,
        arm_split=MASPoseMap(
            default="",
            p1="10",
            p2="5",
            p3="10",
            p4="0",
            p5="10",
            p7="10",
        )
    )
    store.mas_sprites.init_acs(mas_acs_hairties_bracelet_brown)





    mas_acs_heartchoc = MASAccessory(
        "heartchoc",
        "heartchoc",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=False,
        acs_type="chocs",
        mux_type=store.mas_sprites.DEF_MUX_LD,
        keep_on_desk=False
    )
    store.mas_sprites.init_acs(mas_acs_heartchoc)





    mas_acs_hotchoc_mug = MASAccessory(
        "hotchoc_mug",
        "hotchoc_mug",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=True,
        acs_type="mug",
        mux_type=["mug"],
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_hotchoc_mug)





    mas_acs_musicnote_necklace_gold = MASSplitAccessory(
        "musicnote_necklace_gold",
        "musicnote_necklace_gold",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="necklace",
        mux_type=["necklace"],
        ex_props={
            "bare collar": True,
        },
        rec_layer=MASMonika.BSE_ACS,
        arm_split=MASPoseMap(
            default="0",
            use_reg_for_l=True
        )
    )
    store.mas_sprites.init_acs(mas_acs_musicnote_necklace_gold)
    store.mas_selspr.init_selectable_acs(
        acs=mas_acs_musicnote_necklace_gold,
        display_name="Golden Music Note",
        thumb="musicnote_necklace_gold",
        group="necklace",
    )





    mas_acs_diamond_necklace_pink = MASSplitAccessory(
        "diamond_necklace_pink",
        "diamond_necklace_pink",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="necklace",
        mux_type=["necklace"],
        ex_props={
            "bare collar": True,
        },
        rec_layer=MASMonika.BSE_ACS,
        arm_split=MASPoseMap(
            default="0",
            use_reg_for_l=True
        )
    )
    store.mas_sprites.init_acs(mas_acs_diamond_necklace_pink)
    store.mas_selspr.init_selectable_acs(
        acs=mas_acs_diamond_necklace_pink,
        display_name=_("Pink Diamond"),
        thumb="diamond_necklace_pink",
        group="necklace",
    )





    mas_acs_marisa_strandbow = MASAccessory(
        "marisa_strandbow",
        "marisa_strandbow",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="strandbow",
        
        ex_props={
            store.mas_sprites.EXP_A_RQHP: store.mas_sprites.EXP_H_TS,
        },
        rec_layer=MASMonika.AFH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_marisa_strandbow)





    mas_acs_marisa_witchhat = MASAccessory(
        "marisa_witchhat",
        "marisa_witchhat",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="hat",
        
        ex_props={
            store.mas_sprites.EXP_A_RQHP: store.mas_sprites.EXP_H_NT,
            store.mas_sprites.EXP_A_EXCLHP: [store.mas_sprites.EXP_H_TB, store.mas_sprites.EXP_H_WET]
        },
        rec_layer=MASMonika.AFH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_marisa_witchhat)
    store.mas_selspr.init_selectable_acs(
        mas_acs_marisa_witchhat,
        "Witch Hat", 
        "marisa_witchhat",
        "hat",
        select_dlg=[
            _("Ze~"),
            _("Tea time, tea time. Even if we have coffee, it's tea time. Ehehe~"),
            _("Eye of newt, toe of frog..."),
            _("Now where did I leave that broom...")
        ]
    )





    mas_acs_rin_bows_front = MASAccessory(
        "rin_bows_front",
        "rin_bows_front",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ribbon-front",
        mux_type=["ribbon-front"],
        rec_layer=MASMonika.AFH_ACS,
        priority=20
    )
    store.mas_sprites.init_acs(mas_acs_rin_bows_front)





    mas_acs_rin_bows_back = MASAccessory(
        "rin_bows_back",
        "rin_bows_back",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="ribbon-back",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_rin_bows_back)





    mas_acs_rin_ears = MASAccessory(
        "rin_ears",
        "rin_ears",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="headband",
        rec_layer=MASMonika.AFH_ACS,
        priority=5
    )
    store.mas_sprites.init_acs(mas_acs_rin_ears)





    mas_acs_grayhearts_hairclip = MASAccessory(
        "grayhearts_hairclip",
        "grayhearts_hairclip",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="left-hair-clip",
        
        rec_layer=MASMonika.AFH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_grayhearts_hairclip)
    store.mas_selspr.init_selectable_acs(
        mas_acs_grayhearts_hairclip,
        "Hairclip (Gray hearts)",
        "grayhearts_hairclip",
        "left-hair-clip",
        select_dlg=[
            _("My heart beats for you, [player]~"),
            _("Full of love, just like you~")
        ]
    )





    mas_acs_pinkdiamonds_hairclip = MASAccessory(
        "pinkdiamonds_hairclip",
        "pinkdiamonds_hairclip",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="left-hair-clip",
        
        rec_layer=MASMonika.AFH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_pinkdiamonds_hairclip)
    store.mas_selspr.init_selectable_acs(
        mas_acs_pinkdiamonds_hairclip,
        "Hairclip (Pink diamonds)",
        "pinkdiamonds_hairclip",
        "left-hair-clip",
        select_dlg=[
            _("Cute!")
        ]
    )





    mas_acs_holly_hairclip = MASAccessory(
        "holly_hairclip",
        "holly_hairclip",
        MASPoseMap(
            default="0",
            l_default="5"
        ),
        stay_on_start=True,
        acs_type="left-hair-clip",
        
        rec_layer=MASMonika.AFH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_holly_hairclip)
    store.mas_selspr.init_selectable_acs(
        mas_acs_holly_hairclip,
        "Hairclip (Holly)",
        "holly_hairclip",
        "left-hair-clip",
        select_dlg=[
            _("Ready to deck the halls, [player]?")
        ]
    )





    mas_acs_flower_crown = MASAccessory(
        "flower_crown",
        "flower_crown",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        acs_type="front-hair-flower-crown",
        priority=12,
        stay_on_start=True,
        rec_layer=MASMonika.AFH_ACS,
    )
    store.mas_sprites.init_acs(mas_acs_flower_crown)




    mas_acs_promisering = MASSplitAccessory(
        "promisering",
        "promisering",
        MASPoseMap(
            p1=None,
            p2="2",
            p3="3",
            p4=None,
            p5="5",
            p6=None,
            p7=None,
        ),
        stay_on_start=True,
        acs_type="ring",
        rec_layer=MASMonika.ASE_ACS,
        arm_split=MASPoseMap(
            default="",
            p2="10",
            p3="10",
            p5="10"
        ),
        ex_props={
            "bare hands": True
        }
    )
    store.mas_sprites.init_acs(mas_acs_promisering)





    mas_acs_quetzalplushie = MASAccessory(
        "quetzalplushie",
        "quetzalplushie",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=False,
        acs_type="plush_q",
        mux_type=["plush_mid"] + store.mas_sprites.DEF_MUX_LD,
        entry_pp=store.mas_sprites._acs_quetzalplushie_entry,
        exit_pp=store.mas_sprites._acs_quetzalplushie_exit,
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_quetzalplushie)





    mas_acs_quetzalplushie_antlers = MASAccessory(
        "quetzalplushie_antlers",
        "quetzalplushie_antlers",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        priority=12,
        stay_on_start=False,
        entry_pp=store.mas_sprites._acs_quetzalplushie_antlers_entry,
        keep_on_desk=True
    )




    mas_acs_center_quetzalplushie = MASAccessory(
        "quetzalplushie_mid",
        "quetzalplushie_mid",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=False,
        acs_type="plush_mid",
        mux_type=["plush_q"],
        entry_pp=store.mas_sprites._acs_center_quetzalplushie_entry,
        exit_pp=store.mas_sprites._acs_center_quetzalplushie_exit,
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_center_quetzalplushie)





    mas_acs_quetzalplushie_santahat = MASAccessory(
        "quetzalplushie_santahat",
        "quetzalplushie_santahat",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        priority=11,
        stay_on_start=False,
        entry_pp=store.mas_sprites._acs_quetzalplushie_santahat_entry,
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_quetzalplushie_santahat)





    mas_acs_quetzalplushie_center_santahat = MASAccessory(
        "quetzalplushie_santahat_mid",
        "quetzalplushie_santahat_mid",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        priority=11,
        stay_on_start=False,
        entry_pp=store.mas_sprites._acs_center_quetzalplushie_santahat_entry,
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_quetzalplushie_center_santahat)





    mas_acs_ribbon_black = MASAccessory(
        "ribbon_black",
        "ribbon_black",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_black)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_black,
        "Ribbon (Black)",
        "ribbon_black",
        "ribbon",
        hover_dlg=[
            _("That's pretty formal, [player].")
        ],
        select_dlg=[
            _("Are we going somewhere special, [player]?")
        ]
    )





    mas_acs_ribbon_black_gray = MASAccessory(
        "ribbon_black_gray",
        "ribbon_black_gray",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_black_gray)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_black_gray,
        "Ribbon (Black/gray)",
        "ribbon_black_gray",
        "ribbon",
        hover_dlg=[
            _("Very versatile.")
        ],
        select_dlg=[
            _("This goes with so many different outfits!")
        ]
    )





    mas_acs_ribbon_black_pink = MASAccessory(
        "ribbon_black_pink",
        "ribbon_black_pink",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_black_pink)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_black_pink,
        "Ribbon (Black/pink)",
        "ribbon_black_pink",
        "ribbon",
        select_dlg=[
            _("So cute!")
        ]
    )




    mas_acs_ribbon_blank = MASAccessory(
        "ribbon_blank",
        "ribbon_blank",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_blank)





    mas_acs_ribbon_blue = MASAccessory(
        "ribbon_blue",
        "ribbon_blue",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_blue)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_blue,
        "Ribbon (Blue)",
        "ribbon_blue",
        "ribbon",
        hover_dlg=[
            _("Like the ocean...")
        ],
        select_dlg=[
            _("Great choice, [player]!")
        ]
    )





    mas_acs_ribbon_darkpurple = MASAccessory(
        "ribbon_dark_purple",
        "ribbon_dark_purple",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_darkpurple)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_darkpurple,
        "Ribbon (Dark Purple)",
        "ribbon_dark_purple",
        "ribbon",
        hover_dlg=[
            _("I love that color!")
        ],
        select_dlg=[
            _("Lavender is a nice change of pace.")
        ]
    )





    mas_acs_ribbon_emerald = MASAccessory(
        "ribbon_emerald",
        "ribbon_emerald",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_emerald)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_emerald,
        "Ribbon (Emerald)",
        "ribbon_emerald",
        "ribbon",
        hover_dlg=[
            _("I've always loved this color..."),
        ],
        select_dlg=[
            _("It's just like my eyes!")
        ]
    )




    mas_acs_ribbon_def = MASAccessory(
        "ribbon_def",
        "ribbon_def",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_def)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_def,
        "Ribbon (White)",
        "ribbon_def",
        "ribbon",
        hover_dlg=[
            _("Do you miss my old ribbon, [player]?")
        ],
        select_dlg=[
            _("Back to the classics!")
        ]
    )





    mas_acs_ribbon_gray = MASAccessory(
        "ribbon_gray",
        "ribbon_gray",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_gray)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_gray,
        "Ribbon (Gray)",
        "ribbon_gray",
        "ribbon",
        hover_dlg=[
            _("Like a warm, rainy day...")
        ],
        select_dlg=[
            _("That's a really unique color, [player].")
        ]
    )





    mas_acs_ribbon_green = MASAccessory(
        "ribbon_green",
        "ribbon_green",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_green)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_green,
        "Ribbon (Green)",
        "ribbon_green",
        "ribbon",
        hover_dlg=[
            _("That's a lovely color!")
        ],
        select_dlg=[
            _("Green, just like my eyes!")
        ]
    )





    mas_acs_ribbon_lightpurple = MASAccessory(
        "ribbon_light_purple",
        "ribbon_light_purple",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_lightpurple)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_lightpurple,
        "Ribbon (Light Purple)",
        "ribbon_light_purple",
        "ribbon",
        hover_dlg=[
            _("This purple looks pretty nice, right [player]?")
        ],
        select_dlg=[
            _("Really has a spring feel to it.")
        ]
    )





    mas_acs_ribbon_peach = MASAccessory(
        "ribbon_peach",
        "ribbon_peach",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_peach)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_peach,
        "Ribbon (Peach)",
        "ribbon_peach",
        "ribbon",
        hover_dlg=[
            _("That's beautiful!")
        ],
        select_dlg=[
            _("Just like autumn leaves...")
        ]
    )





    mas_acs_ribbon_pink = MASAccessory(
        "ribbon_pink",
        "ribbon_pink",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=[
            "ribbon",
            "bow",
        ],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_pink)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_pink,
        "Ribbon (Pink)",
        "ribbon_pink",
        "ribbon",
        hover_dlg=[
            _("Looks cute, right?")
        ],
        select_dlg=[
            _("Good choice!")
        ]
    )





    mas_acs_ribbon_platinum = MASAccessory(
        "ribbon_platinum",
        "ribbon_platinum",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_platinum)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_platinum,
        "Ribbon (Platinum)",
        "ribbon_platinum",
        "ribbon",
        hover_dlg=[
            _("That's an interesting color, [player]."),
        ],
        select_dlg=[
            _("I'm quite fond of it, actually.")
        ]
    )





    mas_acs_ribbon_red = MASAccessory(
        "ribbon_red",
        "ribbon_red",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_red)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_red,
        "Ribbon (Red)",
        "ribbon_red",
        "ribbon",
        hover_dlg=[
            _("Red is a beautiful color!")
        ],
        select_dlg=[
            _("Just like roses~")
        ]
    )





    mas_acs_ribbon_ruby = MASAccessory(
        "ribbon_ruby",
        "ribbon_ruby",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_ruby)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_ruby,
        "Ribbon (Ruby)",
        "ribbon_ruby",
        "ribbon",
        hover_dlg=[
            _("That's a beautiful shade of red.")
        ],
        select_dlg=[
            _("Doesn't it look pretty?")
        ]
    )





    mas_acs_ribbon_sapphire = MASAccessory(
        "ribbon_sapphire",
        "ribbon_sapphire",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_sapphire)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_sapphire,
        "Ribbon (Sapphire)",
        "ribbon_sapphire",
        "ribbon",
        hover_dlg=[
            _("Like a clear summer sky...")
        ],
        select_dlg=[
            _("Nice choice, [player]!")
        ]
    )





    mas_acs_ribbon_silver = MASAccessory(
        "ribbon_silver",
        "ribbon_silver",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_silver)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_silver,
        "Ribbon (Silver)",
        "ribbon_silver",
        "ribbon",
        hover_dlg=[
            _("I like the look of this one."),
            _("I've always loved silver.")
        ],
        select_dlg=[
            _("Nice choice, [player].")
        ]
    )





    mas_acs_ribbon_teal = MASAccessory(
        "ribbon_teal",
        "ribbon_teal",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_teal)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_teal,
        "Ribbon (Teal)",
        "ribbon_teal",
        "ribbon",
        hover_dlg=[
            _("Looks really summer-y, right?")
        ],
        select_dlg=[
            _("Just like a summer sky.")
        ]
    )





    mas_acs_ribbon_wine = MASAccessory(
        "ribbon_wine",
        "ribbon_wine",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_wine)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_wine,
        "Ribbon (Wine)",
        "ribbon_wine",
        "ribbon",
        hover_dlg=[
            _("That's a great color!")
        ],
        select_dlg=[
            _("Formal! Are you taking me somewhere special, [player]?")
        ]
    )





    mas_acs_ribbon_yellow = MASAccessory(
        "ribbon_yellow",
        "ribbon_yellow",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="ribbon",
        mux_type=["ribbon"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_ribbon_yellow)
    store.mas_selspr.init_selectable_acs(
        mas_acs_ribbon_yellow,
        "Ribbon (Yellow)",
        "ribbon_yellow",
        "ribbon",
        hover_dlg=[
            _("This color reminds me of a nice summer day!")
        ],
        select_dlg=[
            _("Great choice, [player]!")
        ]
    )





    mas_acs_roses = MASAccessory(
        "roses",
        "roses",
        MASPoseMap(
            default="0",
            use_reg_for_l=True
        ),
        priority=11,
        stay_on_start=False,
        acs_type="flowers",
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_roses)





    mas_acs_desk_candy_jack = MASDynamicAccessory(
        "desk_candy_jack",
        ConditionSwitch(
            "(persistent._mas_o31_tt_count + mas_getGiftStatsForDate('mas_reaction_candy', date = mas_o31)) > 2",
            MASFilterableSprite("mod_assets/monika/a/acs-desk_candy_jack_brim-0.png", None),
            "(persistent._mas_o31_tt_count + mas_getGiftStatsForDate('mas_reaction_candy', date = mas_o31)) > 0",
            MASFilterableSprite("mod_assets/monika/a/acs-desk_candy_jack_half-0.png", None),
            "True",
            MASFilterableSprite("mod_assets/monika/a/acs-desk_candy_jack_empty-0.png", None)
        ),
        MASPoseMap(
            default=True,
            l_default=True
        ),
        priority=13,
        acs_type="desk_jack_o_lantern",
        mux_type=["flowers"],
        ex_props={store.mas_sprites.EXP_A_DYNAMIC: True},
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_desk_candy_jack)





    mas_acs_desk_lantern = MASDynamicAccessory(
        "desk_lantern",
        ConditionSwitch(
            "store.mas_isNightNow()", "mod_assets/monika/a/acs-desk_lantern_lit-0.png",
            "True", MASFilterableSprite("mod_assets/monika/a/acs-desk_lantern_unlit-0.png", None)
        ),
        MASPoseMap(
            default=True,
            l_default=True
        ),
        priority=13,
        acs_type="desk_lantern",
        mux_type=store.mas_sprites.DEF_MUX_LD,
        ex_props={store.mas_sprites.EXP_A_DYNAMIC: True},
        keep_on_desk=True
    )
    store.mas_sprites.init_acs(mas_acs_desk_lantern)





    mas_acs_earrings_diamond_pink = MASAccessory(
        "earrings_diamond_pink",
        "earrings_diamond_pink",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        stay_on_start=True,
        acs_type="earrings",
        mux_type=["earrings"],
        rec_layer=MASMonika.BBH_ACS
    )
    store.mas_sprites.init_acs(mas_acs_earrings_diamond_pink)
    store.mas_selspr.init_selectable_acs(
        mas_acs_earrings_diamond_pink,
        "Earrings (Pink Diamond)",
        "earrings_diamond_pink",
        "earrings",
        select_dlg=[
            _("Pretty in pink!"),
            _("I'm shining like a diamond~")
        ]
    )





    mas_acs_water_drops = MASAccessory(
        "water_drops",
        "water_drops",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        acs_type="water-drops",
        priority=1,
        stay_on_start=True,
        rec_layer=MASMonika.MAB_ACS,
    )
    store.mas_sprites.init_acs(mas_acs_water_drops)



init -1 python:




























    mas_clothes_def = MASClothes(
        "def",
        "def",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        entry_pp=store.mas_sprites._clothes_def_entry,
        exit_pp=store.mas_sprites._clothes_def_exit,
        outfit_hair=mas_hair_def,
        outfit_acs=[
            mas_acs_ribbon_def,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_def)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_def,
        "School Uniform",
        "schooluniform",
        "clothes",
        visible_when_locked=True,
        hover_dlg=None,
        select_dlg=[
            _("Ready for school!")
        ]
    )
    store.mas_selspr.unlock_clothes(mas_clothes_def)






    mas_clothes_blackdress = MASClothes(
        "blackdress",
        "blackdress",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_BS: True,
        }
    )
    store.mas_sprites.init_clothes(mas_clothes_blackdress)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_blackdress,
        "Black Dress",
        "blackdress",
        "clothes",
        visible_when_locked=False,
        select_dlg=[
            _("Are we going somewhere special, [player]?")
        ]
    )






    mas_clothes_blackpink_dress = MASClothes(
        "blackpinkdress",
        "blackpinkdress",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_BS: True,
        },
        outfit_hair=mas_hair_def,
        outfit_acs=[
            mas_acs_diamond_necklace_pink,
            mas_acs_pinkdiamonds_hairclip,
            mas_acs_ribbon_black_pink,
            mas_acs_earrings_diamond_pink,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_blackpink_dress)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_blackpink_dress,
        "Black and Pink Dress",
        "blackpinkdress",
        "clothes",
        visible_when_locked=False,
        select_dlg=[
            _("Are we going somewhere special, [player]?")
        ]
    )






    mas_clothes_blazerless = MASClothes(
        "blazerless",
        "blazerless",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_C_DTS: True
        },
        pose_arms=MASPoseArms(
            {
                1: MASArmBoth(
                    "crossed",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
            }
        )
    )
    store.mas_sprites.init_clothes(mas_clothes_blazerless)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_blazerless,
        "School Uniform (Blazerless)",
        "schooluniform_blazerless",
        "clothes",
        visible_when_locked=True,
        hover_dlg=None,
        select_dlg=[
            _("Ah, feels nice without the blazer!"),
        ]
    )
    store.mas_selspr.unlock_clothes(mas_clothes_def)






    mas_clothes_marisa = MASClothes(
        "marisa",
        "marisa",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        pose_arms=MASPoseArms(
            {
                1: MASArmBoth(
                    "crossed",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
                9: MASArmRight(
                    "def",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
            }
        ),
        stay_on_start=True,
        exit_pp=store.mas_sprites._clothes_marisa_exit,
        ex_props={
            store.mas_sprites.EXP_C_C_DTS: True,
            store.mas_sprites.EXP_C_COST: "o31",
            store.mas_sprites.EXP_C_COSP: True,
        },
        outfit_hair=mas_hair_downtiedstrand,
        outfit_acs=[
            mas_acs_marisa_strandbow,
            mas_acs_marisa_witchhat,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_marisa)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_marisa,
        "Witch Costume",
        "marisa",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("Just an ordinary costume, ~ze.")
        ]
    )





    mas_clothes_rin = MASClothes(
        "rin",
        "rin",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        exit_pp=store.mas_sprites._clothes_rin_exit,
        ex_props={
            store.mas_sprites.EXP_C_COST: "o31",
            store.mas_sprites.EXP_C_COSP: True,
            "rin": True 
        },
        outfit_hair=mas_hair_braided,
        outfit_acs=[
            mas_acs_rin_ears,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_rin)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_rin,
        "Neko Costume",
        "rin",
        "clothes",
        visible_when_locked=False,
        hover_dlg=[
            _("~nya?"),
            _("n-nya...")
        ],
        select_dlg=[
            _("Nya!")
        ]
    )



    mas_clothes_spider_lingerie = MASClothes(
        "spider_lingerie",
        "spider_lingerie",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_BS: True,
            "lingerie": "o31"
        },
        pose_arms=MASPoseArms(
            {
                1: MASArmBoth(
                    "crossed",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
                9: MASArmRight(
                    "def",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
            }
        ),
        outfit_hair=mas_hair_def,
        outfit_acs=[
            mas_acs_grayhearts_hairclip,
            mas_acs_ribbon_black_gray,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_spider_lingerie)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_spider_lingerie,
        "Lingerie (Spider)",
        "spider_lingerie",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("Caught you in my web~"),
            _("Don't be scared~"),
            _("Don't worry, I don't bite...")
        ]
    )






    mas_clothes_santa = MASClothes(
        "santa",
        "santa",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            "costume": "d25"
        },
        outfit_hair=mas_hair_def,
        outfit_acs=[
            mas_acs_ribbon_wine,
            mas_acs_holly_hairclip,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_santa)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_santa,
        "Santa Costume",
        "santa",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("Merry Christmas!"),
            _("What kind of {i}presents{/i} do you want?"),
            _("Happy holidays!")
        ]
    )





    mas_clothes_santa_lingerie = MASClothes(
        "santa_lingerie",
        "santa_lingerie",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_BS: True,
            "lingerie": "d25"
        },
        pose_arms=MASPoseArms({}, def_base=False),
        outfit_acs=[
            mas_acs_holly_hairclip,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_santa_lingerie)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_santa_lingerie,
        "Lingerie (Santa)",
        "santa_lingerie",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("Would you like to open your present?~"),
            _("What kind of {i}presents{/i} do you want?"),
            _("Open your present, ehehe~"),
            _("All I want for Christmas is you~"),
            _("Santa baby~"),
            _("What {i}else{/i} do you want to unwrap?~")
        ]
    )





    mas_clothes_dress_newyears = MASClothes(
        "new_years_dress",
        "new_years_dress",
        MASPoseMap(
            default=True,
            use_reg_for_l=True,
        ),
        entry_pp=store.mas_sprites._clothes_dress_newyears_entry,
        exit_pp=store.mas_sprites._clothes_dress_newyears_exit,
        stay_on_start=True,
        pose_arms=MASPoseArms({}, def_base=False),
        ex_props={
            store.mas_sprites.EXP_C_BS: True,
        },
        outfit_hair="orcaramelo_ponytailbraid",
        outfit_acs=[
            mas_acs_flower_crown,
            mas_acs_hairties_bracelet_brown,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_dress_newyears)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_dress_newyears,
        "Dress (New Years)",
        "new_years_dress",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("Are we going somewhere special, [player]?"),
            _("Very formal!"),
            _("Any special occasion, [player]?")
        ],
    )





    mas_clothes_sundress_white = MASClothes(
        "sundress_white",
        "sundress_white",
        MASPoseMap(
            default=True,
            use_reg_for_l=True,
        ),
        stay_on_start=True,
        exit_pp=store.mas_sprites._clothes_sundress_white_exit,
        pose_arms=MASPoseArms({}, def_base=False),
        ex_props={
            store.mas_sprites.EXP_C_BLS: True,
            store.mas_sprites.EXP_C_BRS: True,
        },
        outfit_acs=[
            mas_acs_hairties_bracelet_brown,
            mas_acs_musicnote_necklace_gold,
        ]
    )
    store.mas_sprites.init_clothes(mas_clothes_sundress_white)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_sundress_white,
        "Sundress (White)",
        "sundress_white",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("Are we going anywhere special today, [player]?"),
            _("I've always loved this outfit..."),
        ],
    )





    mas_clothes_vday_lingerie = MASClothes(
        "vday_lingerie",
        "vday_lingerie",
        MASPoseMap(
            default=True,
            use_reg_for_l=True,
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_LING: True,
            store.mas_sprites.EXP_C_BS: True,
        },
        pose_arms=MASPoseArms({}, def_base=False)
    )
    store.mas_sprites.init_clothes(mas_clothes_vday_lingerie)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_vday_lingerie,
        "Lingerie (Pink Lace)",
        "vday_lingerie",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("Ehehe~"),
            _("Do you like what you see, [player]?")
        ]
    )





    mas_clothes_bath_towel_white = MASClothes(
        "bath_towel_white",
        "bath_towel_white",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_BRS: True,
            store.mas_sprites.EXP_C_WET: True
        },
        entry_pp=store.mas_sprites._clothes_bath_towel_white_entry,
        exit_pp=store.mas_sprites._clothes_bath_towel_white_exit,
        pose_arms=MASPoseArms({}, def_base=False)
    )
    store.mas_sprites.init_clothes(mas_clothes_bath_towel_white)





    mas_clothes_nou_shirt = MASClothes(
        "nou_shirt",
        "nou_shirt",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_C_DTS: True
        },
        pose_arms=MASPoseArms(
            {
                9: MASArmRight(
                    "def",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
            }
        )
    )
    store.mas_sprites.init_clothes(mas_clothes_nou_shirt)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_nou_shirt,
        "Shirt (NOU)",
        "nou_shirt",
        "clothes",
        visible_when_locked=False,
        hover_dlg=None,
        select_dlg=[
            _("No U! Ehehe~"),
            _("Ready to draw some more cards?~"),
            _("Colorful!"),
            _("Plus 10 to luck~"),
            _("Up for a game, [player]?")
        ]
    )










default persistent._mas_acs_enable_quetzalplushie = False



default persistent._mas_acs_enable_promisering = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
