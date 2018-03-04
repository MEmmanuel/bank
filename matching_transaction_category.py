from bank.models import Category

category_matching = (
    # SALAIRE
    ('VIREMENT DE SAS LOKI ', Category.objects.get(name='Salaire')),
    ('VIREMENT DE M RALPH BERGERON Avance Salaire Decembre ', Category.objects.get(name='Salaire')),
    ('VIREMENT DE MLE DANA SOTIROVA', Category.objects.get(name='Salaire')),
    ('VIREMENT DE IMPALA', Category.objects.get(name='Salaire')),

    # INTERNE
    ('VIREMENT DE MR MECHIN EMMANUEL ', Category.objects.get(name='Interne')),
    ('VIREMENT POUR MR MECHIN EMMANUEL', Category.objects.get(name='Interne')),
    ('VIREMENT PERMANENT POUR MR MECHIN EMMANUEL', Category.objects.get(name='Interne')),

    # BAR
    ('ACHAT CB HELICE BAR', Category.objects.get(name='Bar')),
    ('ACHAT CB MEPHISTO ', Category.objects.get(name='Bar')),
    ('ACHAT CB TINY CAFE', Category.objects.get(name='Bar')),
    ('ACHAT CB CHEZ FRANCIS', Category.objects.get(name='Bar')),
    ('ACHAT CB CANTINE CIGALE', Category.objects.get(name='Bar')),
    ('ACHAT CB CAFE DES SPORT', Category.objects.get(name='Bar')),
    ('ACHAT CB BAR ROYAL', Category.objects.get(name='Bar')),
    ('ACHAT CB 25 DEGREE EST', Category.objects.get(name='Bar')),
    ('ACHAT CB BIEROCRATIE', Category.objects.get(name='Bar')),
    ('ACHAT CB CHAPICHAPO', Category.objects.get(name='Bar')),
    ('ACHAT CB TAVERNE LA BUT', Category.objects.get(name='Bar')),
    ('ACHAT CB RESERVOIR BIER', Category.objects.get(name='Bar')),
    ('ACHAT CB LE PUB ', Category.objects.get(name='Bar')),
    ('ACHAT CB LE RETROVISEUR', Category.objects.get(name='Bar')),
    ('ACHAT CB AU PERE FOUETT', Category.objects.get(name='Bar')),

    # MUTUELLE
    ('VIREMENT DE LA MUTUELLE GENER MG SANTE809 MECHIN E. SANTE', Category.objects.get(name='Mutuelle')),
    ('PRELEVEMENT DE LA MUTUELLE GENER REF : ', Category.objects.get(name='Mutuelle')),

    # JUNK FOOD
    ('ACHAT CB AUX 3 MERVEILL', Category.objects.get(name='Junk food')),
    ('ACHAT CB QUICK ', Category.objects.get(name='Junk food')),
    ('ACHAT CB MCDONALD S', Category.objects.get(name='Junk food')),
    ('ACHAT CB MC DONALD S', Category.objects.get(name='Junk food')),
    ('ACHAT CB MC DONALDS', Category.objects.get(name='Junk food')),
    ('ACHAT CB MCDONALDS ', Category.objects.get(name='Junk food')),
    ('ACHAT CB BURGER KING', Category.objects.get(name='Junk food')),
    ('ACHAT CB PIZZERIA MASSI', Category.objects.get(name='Junk food')),
    ('ACHAT CB NAGOYA', Category.objects.get(name='Junk food')),
    ('ACHAT CB DELIVEROOFR', Category.objects.get(name='Junk food')),

    # JOURNAUX
    ('ACHAT CB QUESTCE QUON F', Category.objects.get(name='Journaux')),

    # DONS
    ('ACHAT CB SUMOFUS', Category.objects.get(name='Dons')),
    ('ACHAT CB HELLOASSO LW', Category.objects.get(name='Dons')),
    ('AFCP JLM 2017 ', Category.objects.get(name='Dons')),
    ('ACHAT CB BABYLOAN', Category.objects.get(name='Dons')),
    ('VIREMENT DE ABC MICROFINANCE BABYLOAN', Category.objects.get(name='Dons')),

    # ALLOCATIONS
    ('VIREMENT DE CAF DE SEINE ET MARN', Category.objects.get(name='Allocations')),

    # INVESTISSEMENT
    ('ACHAT CB MGP BLUEBEES', Category.objects.get(name='Uber')),

    # UBER
    ('ACHAT CB UBER', Category.objects.get(name='Uber')),

    # INTERÊTS
    ('INTERETS ACQUIS DECOMPTE D\'INTERETS', Category.objects.get(name='Intérêts')),

    # TRANSPORTS
    ('ACHAT CB BlaBlaCar', Category.objects.get(name='Transports')),
    ('PRELEVEMENT DE Navigo Annuel - G COMUTITRES', Category.objects.get(name='Transports')),
    ('ACHAT CB VELIB INTERNET', Category.objects.get(name='Transports')),
    ('ACHAT CB SNCF ', Category.objects.get(name='Transports')),
    ('ACHAT CB OUIBUS', Category.objects.get(name='Transports')),
    ('VIREMENT DE SNCF MOBILITES VOYAG ', Category.objects.get(name='Transports')),

    # FRAIS BANCAIRES
    ('REMISE COMMERCIALE D AGIOS', Category.objects.get(name='Frais bancaires')),
    ('COMMISSION PAIEMENT PAR CARTE', Category.objects.get(name='Frais bancaires')),
    ('MINIMUM FORFAITAIRE TRIMESTRIEL D UTILISATION DU DECOUVERT', Category.objects.get(name='Frais bancaires')),
    ('COTISATION TRIMESTRIELLE DE VOTRE FORMULE DE COMPTE', Category.objects.get(name='Frais bancaires')),

    # IMPÔTS
    ('PRELEVEMENTS SOCIAUX DECOMPTE D\'INTERETS', Category.objects.get(name='Impôts et taxes')),
    ('ACHAT CB AMENDE RADAR', Category.objects.get(name='Impôts et taxes')),
    ('ACHAT CB URSSAF IDF', Category.objects.get(name='Impôts et taxes')),

    # ALIMENTATION
    ('ACHAT CB WELCOME BIO', Category.objects.get(name='Alimentation')),
    ('ACHAT CB SHINE GARDEN', Category.objects.get(name='Alimentation')),
    ('ACHAT CB MONOPRIX', Category.objects.get(name='Alimentation')),
    ('ACHAT CB LE PLATEAU D A', Category.objects.get(name='Alimentation')),
    ('ACHAT CB LA VIE EN BIO', Category.objects.get(name='Alimentation')),

    # RETRAIT
    (' RETRAIT DAB ', Category.objects.get(name='Retrait')),
    ('ACHAT CB PAYPAL', Category.objects.get(name='Retrait')),

    # RESTAURANT
    ('ACHAT CB BISTRO REGENT', Category.objects.get(name='Restaurant')),

    # SANTE
    ('VIREMENT DE HARMONIE MUT', Category.objects.get(name='Santé')),
    ('ACHAT CB APHPTIPI', Category.objects.get(name='Santé')),
    ('ACHAT CB PHARMACIE ', Category.objects.get(name='Santé')),

    # HABILLEMENT
    ('ACHAT CB SACRES COUPONS', Category.objects.get(name='Santé')),
    ('ACHAT CB COUPONS PARIS', Category.objects.get(name='Santé')),

    # FRAIS PROFESSIONNELS
    ('ACHAT CB JetBrains', Category.objects.get(name='Frais professionnels')),
    ('ACHAT CB MACINCLOUD.COM', Category.objects.get(name='Frais professionnels')),
    ('ACHAT CB ALWAYSDATA', Category.objects.get(name='Frais professionnels')),
    ('VIREMENT POUR ALWAYSDATA', Category.objects.get(name='Frais professionnels')),
    ('VIREMENT PERMANENT POUR ALWAYSDATA', Category.objects.get(name='Frais professionnels')),
    ('VIREMENT POUR MR GUESNE VINCENT', Category.objects.get(name='Frais professionnels')),

    # CADEAUX
    ('ACHAT CB LOU YETU', Category.objects.get(name='Cadeaux')),

    # EVENEMENTS
    ('ACHAT CB DIGITICK SA', Category.objects.get(name='Evénements')),

    # ELECTRONIQUE
    ('ACHAT CB COMMOWN', Category.objects.get(name='Eléctronique')),


    # RESTE
    # ('ACHAT CB INTERMARCHE', Category.objects.get(name='Alimentation')),
    # ('ACHAT CB CARREFOURMARKE', Category.objects.get(name='Alimentation')),
    # ('ACHAT CB FNAC ST LAZARE ', Category.objects.get(name='Alimentation')),
    # ('ACHAT CB FNAC DIRECT', Category.objects.get(name='Alimentation')),
    # ('ACHAT CB LE TSHIRT PROP', Category.objects.get(name='Habillement')),
)
