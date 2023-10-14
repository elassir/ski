#Poids des remontee:
#telepherique: 5
#telecabine: 6
#telesiège: 7
#tele ski: 8

#Poids des pistes:
#pour les debutants:On prend le carre de la vitesse d'un skieur confirmé
#piste verte: 1
#piste bleue: 4
#piste rouge: 9
#piste noire: 16
#pour les confirmes:
#piste verte: 1
#piste bleue: 2
#piste rouge: 3
#piste noire: 4

TELEPHERIQUE = 5
TELECABINE = 6
TELESIEGE = 7
TELESKI = 8

def build_graphe(VERTE, BLEUE, ROUGE, NOIRE):
    graphe = {
    "haut_roc_merlet": {
        "creux": {
            "chanrossa": NOIRE,
            "Jean Pachod": ROUGE
            },
        "haut_pyramide": {"pyramide": ROUGE},
        },
    "haut_pyramide": {
        "haut_roc_merlet": {"roc merlet": TELESIEGE},
        "haut_combe": {
            "plan mugnier": BLEUE,
            "mont russes": BLEUE,
            "pyramide": BLEUE
        }
        },
    "creux": {
        "vizelle": {"marmottes": TELESIEGE},
        "prameruel": {"creux": ROUGE}
        },
    "signal": {
        "bas_chapelets": {
            "chapelets": ROUGE,
            "rochers": ROUGE,
            },
        "bel_air": {
            "rocher": ROUGE,
            "grandes bosses": BLEUE
            },
        "haut_combe": {"grandes bosses": BLEUE}
        },
    "haut_combe": {
        "prameruel": {"roc mugnier": ROUGE},
        "bel_air": {"No name": BLEUE},
        "bosses": {"grandes bosses": BLEUE},
        "haut_pyramide": {"pyramide": TELESIEGE},
        },
    "bas_combe": {
        "haut_combe": {"combe": TELESKI},
        },
    "bas_chapelets": {
        "signal": {"signal": TELESIEGE},
        "bosses": {"praline": VERTE},
        "bas_stade": {"praline": VERTE}
        },
    "courchevel_1650": {
        "bosses": {
            "3 vallees": TELESIEGE,
            "marquis": TELESIEGE
            },
        "bel_air": {"ariondaz": TELECABINE},
        "haut_st_aggate": {"st agathe": TELESKI},
        "haut_belvedere": {"belvedere": TELESKI}
        },
    "haut_belvedere": {
        "bas_stade": {"No name": VERTE},
        "courchevel_1650": {"belvedere": VERTE}
        },
    "bas_stade": {
        "bosses": {"granges": TELESKI},
        "courchevel_1650": {"belvedere": VERTE}
        },
    "haut_st_aggate": {
        "courchevel_1650": {"marquis": BLEUE}
        },
    "bosses": {
        "signal": {"signal": TELESIEGE},
        "prameruel": {"pte bosse": TELESKI},
        "courchevel_1650": {
            "indiens": BLEUE,
            "piste bleue": BLEUE
            },
        "bas_stade": {"granges": BLEUE}
        },
    "bel_air": {
        "prameruel": {"No name": VERTE},
        "bas_chapelets": {
            "bel air": ROUGE,
            "rocher": ROUGE
            },
        "bosses": {"ariondaz": BLEUE},
        "bas_combe": {"No name": VERTE}
        },
    "prameruel": {
        "haut_combe": {"roc mugnier": TELESIEGE},
        "haut_gravelle": {"gravelles": TELESIEGE},
        "haut_aiguille_du_fruit": {"aguille du fruit": TELESIEGE}
        },
    "haut_gravelle": {
        "bas_suisse": {"altiport": BLEUE},
        "prameruel": {"cave des creux": ROUGE}
        },
    "haut_aiguille_du_fruit": {
        "haut_gravelle": {"park city": ROUGE},
        "bas_suisse": {"suisse": NOIRE},
        "creux": {"rama": ROUGE},
        "bas_creux_noirs": {"No name": ROUGE}
        },
    "bas_suisse": {
        "prameruel": {"mur": ROUGE},
        "pralong": {"No name": BLEUE},
        "vizelle": {"suisses": TELESIEGE}
        },
    "vizelle": {
        "bas_creux_noirs": {"creux": ROUGE},
        "verdons": {"m": NOIRE},
        "saulire": {"No name": ROUGE},
        "bas_suisse": {"suisses": NOIRE},
        "haut_aiguille_du_fruit": {"turcs": NOIRE},
        "creux": {"park city": ROUGE},
        "haut_rocher_ombre": {
            "combe pylones": NOIRE,
            "combe saulire": ROUGE
            }
        },
    "creux_noirs": {
        "bas_creux_noirs": {
            "creux": ROUGE,
            "roches grises": NOIRE
        }
        },
    "bas_creux_noirs": {
        "creux": {"creux": ROUGE},
        "haut_gravelle": {"lac creux": ROUGE},
        "creux_noirs": {"creux noirs": TELESIEGE},
        },
    "saulire": {
        "bas_creux_noirs": {"creux": ROUGE},
        "haut_rocher_ombre": {"grand couloir": NOIRE},
        },
    "haut_biollay": {
        "bas_suisse": {"super pralong": BLEUE},
        "pralong": {
            "pralong": BLEUE,
            "biollay": BLEUE
            },
        "prameruel": {"prameruel": BLEUE},
        "verdons": {"biolay verdons": BLEUE},
        "lac": {
            "marquetty": ROUGE,
            "biolay": BLEUE
            },
        },
    "verdons": {
        "vizelle": {"vizelle": TELECABINE},
        "saulire": {"saulire": TELEPHERIQUE},
        "lac": {
            "verdons": VERTE,
            "renard": VERTE
            },
        "haut_bellecote": {"renard": VERTE}
        },
    "pralong": {
        "haut_biollay": {"pralong": TELESIEGE}
        },
    "lac": {
        "haut_biollay": {"biolay": TELESIEGE},
        "chenus": {"coqs": TELESIEGE},
        "haut_rocher_ombre": {"rocher de l'ombre": TELESKI},
        "courchevel_1850": {"No name": VERTE},
        "haut_bellecote": {"jardin alpin": TELECABINE}
        },
    "haut_bellecote": {
        "lac": {"No name": VERTE},
        "courchevel_1850": {"No name": VERTE},
        "pralong": {"No name": VERTE}
        },
    "haut_rocher_ombre": {
        "verdons": {"No name": ROUGE},
        "lac": {
            "stade descente": ROUGE,
            "No name": ROUGE    
            }
        },
    "courchevel_1850": {
        "haut_bellecote": {
            "jardin alpin": TELECABINE,
            "bellecote": TELESKI
            },
        "lac": {"jardin alpin": TELECABINE},
        "verdons": {"verdons": TELECABINE},
        "chenus": {"chenus": TELECABINE},
        "loze": {"loze": TELESKI},
        "courchevel_1550": {
            "proveres": BLEUE,
            "tovets": BLEUE,
            "stade": BLEUE
            },
        "bas_plantrey": {"No name": VERTE}
        },
    "chenus": {
        "col_loze": {"col de la loze": TELESIEGE},
        "lac": {
            "anemone": BLEUE,
            "chenus": ROUGE
            },
        "courchevel_1850": {"anemone": BLEUE},
        "loze": {"No name": BLEUE},
        "praz_juget": {"lanches": ROUGE}
        },
    "loze": {
        "lac": {"loze est": VERTE},
        "haut_foret": {"cretes": BLEUE},
        "bas_plantrey": {"dou du midi": ROUGE},
        "courchevel_1850": {"loze": ROUGE},
        "praz_juget": {"bouc blanc": ROUGE},
        "courchevel_1550": {"jean blanc": NOIRE},
        "courchevel_1300": {"jean blanc": NOIRE},
        "st_bon": {"jean blanc": NOIRE},
        },
    "courchevel_1550": {
        "courchevel_1850": {
            "grangettes": TELECABINE,
            "tovets": TELESIEGE
        }
        },
    "bas_plantrey": {
        "courchevel_1550": {"don du midi": ROUGE},
        "courchevel_1300": {"brigues": ROUGE},
        "st_bon": {"saint bon": ROUGE},
        "loze": {"plantrey": TELESIEGE},
        "haut_epicea": {"epicea": TELESKI}
        },
    "haut_epicea": {
        "bas_plantrey": {"No name": VERTE},
        "courchevel_1850": {"No name": VERTE}
        },
    "courchevel_1300": {
        "haut_foret": {"foret": TELECABINE},
        "bas_plantrey": {"praz": TELECABINE}
        },
    "st_bon": {
        },
    "haut_foret": {
        "bas_plantrey": {"don du midi": ROUGE},
        "loze": {"cretes": TELESIEGE},
        "praz_juget": {"arolles": BLEUE},
        "courchevel_1300": {"jean blanc": NOIRE},
        "courchevel_1550": {"jean blanc": NOIRE},
        "st_bon": {"jean blanc": NOIRE}
        },
    "col_loze": {
        "chenus": {"col de la loze": BLEUE},
        "praz_juget": {"douu des lanches": NOIRE},
        },
    "praz_juget": {
        "col_loze": {"dou des lanches": TELESIEGE},
        "chenus": {"praz juget": TELESKI},
        "la tania": {
            "moretta blanche": ROUGE,
            "folyeres": BLEUE,
            "plan fontaine": VERTE
            },
        "courchevel_1300": {
            "jockeys": NOIRE,
            "murettes": ROUGE
        }
        },
    "la tania": {
        "praz_juget": {"la tania": TELECABINE},
    }
    }
    return graphe