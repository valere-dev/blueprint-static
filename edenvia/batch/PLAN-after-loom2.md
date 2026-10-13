# Plan de changement après le Loom 2 (U1–U101 reviewés, 2026-10-11)

Score : 66 validées sur 101 (65 % du premier coup), 35 à refaire. Les 35 ratés se répartissent en 6 erreurs récurrentes.

## Les 6 erreurs et la correction de chacune

| # | Erreur | Ads | Cause réelle | Correction |
|---|---|---|---|---|
| 1 | **Comparaison nous contre nous** (us vs them, old me / new me, avant/après produit) : Edenvia des deux côtés | U2 U4 U6 U9 U10 U11 U15 | le rédacteur de prompts n'avait aucun "produit rival" à décrire | un **asset rival** généré une fois et stocké (`assets/product/rival/`) : un flacon blanc générique "WATER PILLS", un pot de gummies, un pot de pilules, sans marque. Règle dans le brief : *gauche = ce qui échoue (rival + ce que l'avatar subit), droite = Edenvia + ce qu'elle désire*. Jamais Edenvia à gauche. |
| 2 | **Mauvais pouch / mauvais logo** : le modèle a dessiné un autre sachet ou un faux logo | U12 U20 U21 U32 U45 U51 U58 U62 U66 U69 U80 U92 U95 U101 | la photo studio n'était pas toujours en référence (prompts "No product"), et le logo n'a jamais été passé en référence | **toujours** 2 références : pouch studio + fichier logo officiel. Quand la template a un slot logo, le vrai fichier est collé par script après génération (0 crédit). **Contrôle automatique** : un modèle vision compare le pouch généré à la photo (icône, "Edenvia", "8PPM") et relance seul jusqu'à 2 fois. |
| 3 | **Texte non adapté** (headline ou bénéfices de la template gardés : chin hair, biotin, gut, sugar, app) | U27 U37 U39 U43 U56 U60 U80 U81 U82 U95 | le rédacteur de prompts a recopié les lignes de la template | règle dure : *chaque ligne de texte est réécrite pour l'avatar, aucune ligne de la template ne survit telle quelle* + **validateur** avant génération : toute ligne identique à la template, ou contenant un mot d'une autre niche (hair, chin, gut, sugar, collagen, biotin, acne, app, snack…), bloque et renvoie le prompt à la réécriture. |
| 4 | **Features au lieu de marketing** (texte mou, "helps", features produit) | U11 U51 U70 | brief trop descriptif | section "ton" dans le brief : *vendre, pas décrire* ; verbes d'action ("drains", "triggers"), urgence, le désir de l'avatar plutôt que la caractéristique. Liste de bénéfices toujours ≥ celle de la template. |
| 5 | **Offre / prix / code pas à nous** | U66 U85 U87 U90 | le rédacteur a gardé l'offre de la template | validateur : tout `$`, `%` ou "code" hors de la liste autorisée bloque ; un code promo devient une remise, un prix ou un bénéfice. |
| 6 | **Ingrédients inventés** | U71 | le modèle a copié la liste d'ingrédients de la template | brief : *les seuls ingrédients nommables sont hydrogène, magnésium, minéraux*. Validateur sur une liste noire (shilajit, boron, zinc, tongkat, …). |

Divers : anatomie (U78 trois jambes) → le contrôle vision le détecte et relance ; "2025" → année courante dans le brief ; U98 (UGC organique) → le rédacteur doit respecter le format natif sans ajouter de produit.

## Le nouveau pipeline (un ad = 1 à 3 appels, tout automatique)

1. **Analyse** de la template par le modèle vision : format, famille, mécanisme, *et le rôle de chaque zone* (rival / nous, avant / après, douleur / désir).
2. **Prompt** écrit avec le brief v2 (règles 1 à 6 ci-dessus), références = template + pouch studio + logo (+ asset rival si comparaison).
3. **Validateur texte** (sans crédit) : lignes identiques, mots d'autres niches, prix, ingrédients → renvoi en réécriture.
4. **Génération** kie gpt-image-2.
5. **Contrôle vision** de l'image (sans crédit kie, ~0,002 $) : bon pouch, logo, texte attendu présent, anatomie, pas de produit rival à droite → relance jusqu'à 2 fois, puis signalé.
6. Collage du logo officiel par script quand il y a un slot.

Coût attendu : ~1,5 appel par ad au lieu de 1,1, soit 9 crédits (0,05 $) par ad. Objectif : passer de 65 % à 90 % du premier coup.

## Ce que je lance si vous validez

- Construire l'asset rival, le validateur et le contrôle vision (1 h).
- Refaire les 35 ratées, puis passer les 169 non reviewées (U102–U270) dans le nouveau contrôle et refaire celles qu'il rejette.
- Reporter le coût et republier les deux pages complètes.
