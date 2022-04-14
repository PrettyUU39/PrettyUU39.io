import matplotlib.pyplot as plt
import numpy as np
consolelist = [1649401650927,1649401650937,1649401650958,1649401650990,1649401650997,1649401651017,1649401651039,1649401651058,1649401651078,1649401651098,1649401651122,1649401651140,1649401651158,1649401651178,1649401651198,1649401651219,1649401651238,1649401651258,1649401651279,1649401651299,1649401651319,1649401651339,1649401651359,1649401651379,1649401651399,1649401651419,1649401651439,1649401651460,1649401651480,1649401651500,1649401651521,1649401651542,1649401651561,1649401651582,1649401651601,1649401651621,1649401651641,1649401651661,1649401651681,1649401651701,1649401651798,1649401651847,1649401651848,1649401651848,1649401651849,1649401651849,1649401651849,1649401651900,1649401651912,1649401651912,1649401651923,1649401651944,1649401651963,1649401651983,1649401652003,1649401652024,1649401652044,1649401652064,1649401652084,1649401652105,1649401652124,1649401652144,1649401652164,1649401652185,1649401652205,1649401652225,1649401652245,1649401652265,1649401652285,1649401652305,1649401652325,1649401652346,1649401652366,1649401652386,1649401652406,1649401652427,1649401652446,1649401652476,1649401652487,1649401652507,1649401652527,1649401652547,1649401652567,1649401652588,1649401652608,1649401652628,1649401652649,1649401652668,1649401652689,1649401652708,1649401652728,1649401652750,1649401652768,1649401652790,1649401652809,1649401652829,1649401652849,1649401652869,1649401652891,1649401652909,1649401652929,1649401652951,1649401652971,1649401652992,1649401653010,1649401653030,1649401653051,1649401653071,1649401653092,1649401653111,1649401653131,1649401653151,1649401653171,1649401653191,1649401653211,1649401653232,1649401653252,1649401653272,1649401653293,1649401653312,1649401653332,1649401653354,1649401653372,1649401653394,1649401653413,1649401653433,1649401653454,1649401653473,1649401653494,1649401653514,1649401653534,1649401653555,1649401653574,1649401653594,1649401653616,1649401653634,1649401653658,1649401653675,1649401653696,1649401653716,1649401653735,1649401653757,1649401653776,1649401653797,1649401653816,1649401653836,1649401653856,1649401653876,1649401653896,1649401653917,1649401653936,1649401653958,1649401653977,1649401653997,1649401654019,1649401654038,1649401654059,1649401654078,1649401654099,1649401654118,1649401654138,1649401654160,1649401654179,1649401654198,1649401654220,1649401654239,1649401654260,1649401654279,1649401654299,1649401654320,1649401654339,1649401654360,1649401654379,1649401654399,1649401654421,1649401654440,1649401654461,1649401654482,1649401654500,1649401654520,1649401654540,1649401654562,1649401654581,1649401654601,1649401654622,1649401654641,1649401654663,1649401654683,1649401654701,1649401654723,1649401654742,1649401654774,1649401654782,1649401654802,1649401654824,1649401654843,1649401654863,1649401654884,1649401654903,1649401654924,1649401654943,1649401654963,1649401654984,1649401655004,1649401655026,1649401655044,1649401655064,1649401655085,1649401655104,1649401655126,1649401655145,1649401655165,1649401655186,1649401655205,1649401655226,1649401655245,1649401655265,1649401655291,1649401655306,1649401655327,1649401655346,1649401655366,1649401655386,1649401655406,1649401655426,1649401655447,1649401655467,1649401655487,1649401655507,1649401655529,1649401655547,1649401655568,1649401655588,1649401655608,1649401655629,1649401655648,1649401655668,1649401655689,1649401655708,1649401655730,1649401655749,1649401655769,1649401655790,1649401655809,1649401655830,1649401655851,1649401655869,1649401655891,1649401655910,1649401655930,1649401655951,1649401655970,1649401655995,1649401656010,1649401656031,1649401656052,1649401656071,1649401656092,1649401656112,1649401656132,1649401656153,1649401656171,1649401656192,1649401656212,1649401656232,1649401656253,1649401656272,1649401656293,1649401656314,1649401656333,1649401656354,1649401656373,1649401656395,1649401656413,1649401656433,1649401656454,1649401656473,1649401656494,1649401656514,1649401656535,1649401656554,1649401656574,1649401656595,1649401656616,1649401656635,1649401656659,1649401656675,1649401656696,1649401656715,1649401656735,1649401656757,1649401656776,1649401656796,1649401656816,1649401656836,1649401656856,1649401656876,1649401656896,1649401656917,1649401656937,1649401656957,1649401656977,1649401656997,1649401657017,1649401657037,1649401657058,1649401657078,1649401657098,1649401657118,1649401657138,1649401657160,1649401657178,1649401657198,1649401657219,1649401657239,1649401657259,1649401657279,1649401657299,1649401657319,1649401657339,1649401657359,1649401657380,1649401657400,1649401657420,1649401657440,1649401657460,1649401657480,1649401657500,1649401657520,1649401657541,1649401657561,1649401657581,1649401657602,1649401657622,1649401657641,1649401657663,1649401657682,1649401657702,1649401657723,1649401657742,1649401657763,1649401657783,1649401657804,1649401657824,1649401657843,1649401657864,1649401657883,1649401657903,1649401657925,1649401657943,1649401657964,1649401657986,1649401658004,1649401658025,1649401658044,1649401658065,1649401658086,1649401658104,1649401658126,1649401658145,1649401658165,1649401658187,1649401658206,1649401658227,1649401658246,1649401658266,1649401658286,1649401658306,1649401658326,1649401658346,1649401658366,1649401658387,1649401658407,1649401658427,1649401658447,1649401658467,1649401658487,1649401658507,1649401658527,1649401658547,1649401658568,1649401658588,1649401658608,1649401658628,1649401658648,1649401658669,1649401658690,1649401658709,1649401658730,1649401658750,1649401658770,1649401658790,1649401658809,1649401658830,1649401658850,1649401658870,1649401658891,1649401658910,1649401658931,1649401658952,1649401658971,1649401658992,1649401659011,1649401659032,1649401659051,1649401659071,1649401659092,1649401659111,1649401659132,1649401659153,1649401659172,1649401659193,1649401659212,1649401659233,1649401659254,1649401659272,1649401659293,1649401659313,1649401659333,1649401659354,1649401659373,1649401659395,1649401659413,1649401659433,1649401659455,1649401659474,1649401659496,1649401659514,1649401659534,1649401659556,1649401659575,1649401659597,1649401659616,1649401659635,1649401659657,1649401659675,1649401659697,1649401659716,1649401659737,1649401659757,1649401659776,1649401659797,1649401659816,1649401659836,1649401659858,1649401659877,1649401659898,1649401659917,1649401659937,1649401659961,1649401659977,1649401659999,1649401660018,1649401660038,1649401660058,1649401660079,1649401660099,1649401660118,1649401660138,1649401660160,1649401660178,1649401660200,1649401660220,1649401660239,1649401660260,1649401660280,1649401660300,1649401660320,1649401660340,1649401660361,1649401660380,1649401660400,1649401660421,1649401660440,1649401660461,1649401660481,1649401660501,1649401660522,1649401660541,1649401660562,1649401660581,1649401660602,1649401660622,1649401660642,1649401660663,1649401660683,1649401660703,1649401660723,1649401660742,1649401660765,1649401660783,1649401660805,1649401660825,1649401660843,1649401660869,1649401660883,1649401660905,1649401660925,1649401660944,1649401660966,1649401660984,1649401661005,1649401661025,1649401661045,1649401661066,1649401661087,1649401661106,1649401661125,1649401661145,1649401661166,1649401661186,1649401661206,1649401661226,1649401661246,1649401661271,1649401661286,1649401661306,1649401661328,1649401661347,1649401661369,1649401661387,1649401661408,1649401661427,1649401661447,1649401661469,1649401661488,1649401661508,1649401661531,1649401661548,1649401661569,1649401661589,1649401661608,1649401661629,1649401661649,1649401661670,1649401661689,1649401661709,1649401661730,1649401661751,1649401661771,1649401661790,1649401661810,1649401661831,1649401661851,1649401661870,1649401661894,1649401661910,1649401661932,1649401661951,1649401661971,1649401661992,1649401662011,1649401662032,1649401662051,1649401662072,1649401662093,1649401662112,1649401662133,1649401662152,1649401662173,1649401662194,1649401662212,1649401662234,1649401662253,1649401662273,1649401662294,1649401662313,1649401662334,1649401662353,1649401662374,1649401662394,1649401662416,1649401662434,1649401662454,1649401662474,1649401662494,1649401662515,1649401662535,1649401662555,1649401662576,1649401662595,1649401662616,1649401662635,1649401662656,1649401662677,1649401662696,1649401662717,1649401662736,1649401662756,1649401662776,1649401662796,1649401662818,1649401662838,1649401662860,1649401662877,1649401662898,1649401662917,1649401662937,1649401662959,1649401662978,1649401662999,1649401663018,1649401663038,1649401663058,1649401663078,1649401663101,1649401663119,1649401663139,1649401663159,1649401663179,1649401663201,1649401663219,1649401663239,1649401663261,1649401663280,1649401663301,1649401663320,1649401663340,1649401663362,1649401663380,1649401663402,1649401663421,1649401663441,1649401663462,1649401663481,1649401663501,1649401663521,1649401663541,1649401663563,1649401663582,1649401663602,1649401663622,1649401663642,1649401663663,1649401663682,1649401663703,1649401663724,1649401663743,1649401663764,1649401663783,1649401663803,1649401663825,1649401663843,1649401663868,1649401663884,1649401663904,1649401663925,1649401663944,1649401663966,1649401663984,1649401664005,1649401664026,1649401664045,1649401664067,1649401664085,1649401664105,1649401664126,1649401664145,1649401664168,1649401664186,1649401664206,1649401664228,1649401664246,1649401664270,1649401664287,1649401664307,1649401664328,1649401664347,1649401664369,1649401664387,1649401664407,1649401664429,1649401664448,1649401664469,1649401664488,1649401664508,1649401664530,1649401664548,1649401664568,1649401664589,1649401664609,1649401664630,1649401664649,1649401664669,1649401664689,1649401664709,1649401664731,1649401664750,1649401664771,1649401664790,1649401664810,1649401664830,1649401664850,1649401664870,1649401664891,1649401664911,1649401664932,1649401664951,1649401664971,1649401664993,1649401665011,1649401665033,1649401665052,1649401665072,1649401665093,1649401665112,1649401665134,1649401665152,1649401665173,1649401665194,1649401665213,1649401665234,1649401665253,1649401665273,1649401665295,1649401665313,1649401665335,1649401665354,1649401665374,1649401665395,1649401665414,1649401665436,1649401665455,1649401665475,1649401665496,1649401665515,1649401665536,1649401665555,1649401665575,1649401665596,1649401665616,1649401665637,1649401665656,1649401665677,1649401665696,1649401665717,1649401665737,1649401665758,1649401665777,1649401665798,1649401665817,1649401665837,1649401665858,1649401665878,1649401665898,1649401665919,1649401665939,1649401665960,1649401665978,1649401665999,1649401666018,1649401666038,1649401666060,1649401666079,1649401666100,1649401666119,1649401666139,1649401666159,1649401666179,1649401666201,1649401666220,1649401666240,1649401666260,1649401666280,1649401666302,1649401666321,1649401666340,1649401666362,1649401666381,1649401666402,1649401666421,1649401666441,1649401666463,1649401666481,1649401666503,1649401666522,1649401666542,1649401666562,1649401666583,1649401666603,1649401666623,1649401666642,1649401666663,1649401666683,1649401666704,1649401666728,1649401666743,1649401666765,1649401666784,1649401666804,1649401666908,1649401666954,1649401666954,1649401666954,1649401666955,1649401666955,1649401666955,1649401666965,1649401666985,1649401667005,1649401667028,1649401667045,1649401667066,1649401667086,1649401667106,1649401667127,1649401667146,1649401667167,1649401667188,1649401667208,1649401667228,1649401667247,1649401667268,1649401667287,1649401667307,1649401667328,1649401667347,1649401667369,1649401667388,1649401667409,1649401667430,1649401667448,1649401667470,1649401667488,1649401667509,1649401667530,1649401667549,1649401667570,1649401667589,1649401667610,1649401667630,1649401667649,1649401667671,1649401667690,1649401667711,1649401667731,1649401667750,1649401667771,1649401667791,1649401667812,1649401667832,1649401667851,1649401667872,1649401667892,1649401667912,1649401667933,1649401667951,1649401667974,1649401667993,1649401668012,1649401668033,1649401668052,1649401668073,1649401668094,1649401668113,1649401668134,1649401668153,1649401668173,1649401668195,1649401668213,1649401668235,1649401668253,1649401668274,1649401668294,1649401668314,1649401668336,1649401668354,1649401668375,1649401668395,1649401668415,1649401668436,1649401668455,1649401668475,1649401668496,1649401668515,1649401668537,1649401668556,1649401668576,1649401668597,1649401668616,1649401668637,1649401668656,1649401668676,1649401668698,1649401668717,1649401668739,1649401668757,1649401668778,1649401668798,1649401668817,1649401668839,1649401668858,1649401668878,1649401668899,1649401668918,1649401668939,1649401668958,1649401668979,1649401669000,1649401669019,1649401669040,1649401669062,1649401669079,1649401669100,1649401669120,1649401669140,1649401669161,1649401669180,1649401669201,1649401669220,1649401669241,1649401669260,1649401669281,1649401669302,1649401669321,1649401669341,1649401669363,1649401669381,1649401669402,1649401669421,1649401669442,1649401669463,1649401669482,1649401669503,1649401669522,1649401669543,1649401669563,1649401669583,1649401669604,1649401669623,1649401669644,1649401669664,1649401669683,1649401669705,1649401669724,1649401669744,1649401669765,1649401669784,1649401669806,1649401669824,1649401669844,1649401669866,1649401669885,1649401669906,1649401669925,1649401669945,1649401669966,1649401669985,1649401670007,1649401670027,1649401670046,1649401670067,1649401670086,1649401670107,1649401670126,1649401670146,1649401670172,1649401670189,1649401670207,1649401670227,1649401670247,1649401670267,1649401670287,1649401670316,1649401670328,1649401670348,1649401670369,1649401670388,1649401670410,1649401670428,1649401670448,1649401670470,1649401670489,1649401670510,1649401670530,1649401670549,1649401670571,1649401670589,1649401670609,1649401670630,1649401670650,1649401670671,1649401670690,1649401670712,1649401670730,1649401670751,1649401670771,1649401670791,1649401670811,1649401670831,1649401670853,1649401670871,1649401670892,1649401670913,1649401670932,1649401670952,1649401670972,1649401670995,1649401671012,1649401671033,1649401671053,1649401671073,1649401671093,1649401671114,1649401671133,1649401671155,1649401671175,1649401671195,1649401671214,1649401671236,1649401671254,1649401671274,1649401671294,1649401671315,1649401671336,1649401671355,1649401671375,1649401671395,1649401671415,1649401671437,1649401671455,1649401671476,1649401671496,1649401671516,1649401671537,1649401671556,1649401671577,1649401671597,1649401671617,1649401671638,1649401671657,1649401671678,1649401671697,1649401671717,1649401671738,1649401671757,1649401671778,1649401671799,1649401671818,1649401671840,1649401671858,1649401671878,1649401671898,1649401671918,1649401671941,1649401671959,1649401671979,1649401672001,1649401672019,1649401672041,1649401672060,1649401672080,1649401672102,1649401672120,1649401672142,1649401672160,1649401672180,1649401672202,1649401672221,1649401672242,1649401672261,1649401672281,1649401672303,1649401672321,1649401672343,1649401672362,1649401672382,1649401672403,1649401672422,1649401672442,1649401672462,1649401672482,1649401672504,1649401672523,1649401672544,1649401672563,1649401672583,1649401672605,1649401672623,1649401672643,1649401672665,1649401672684,1649401672706,1649401672724,1649401672744,1649401672766,1649401672784,1649401672813,1649401672825,1649401672845,1649401672867,1649401672885,1649401672908,1649401672925,1649401672946,1649401672966,1649401672986,1649401673008,1649401673026,1649401673046,1649401673067,1649401673087,1649401673108,1649401673127,1649401673147,1649401673169,1649401673187,1649401673209,1649401673227,1649401673248,1649401673269,1649401673288,1649401673309,1649401673328,1649401673349,1649401673369,1649401673389,1649401673410,1649401673429,1649401673449,1649401673471,1649401673489,1649401673510,1649401673530,1649401673552,1649401673570,1649401673590,1649401673611,1649401673630,1649401673650,1649401673672,1649401673691,1649401673712,1649401673733,1649401673751,1649401673773,1649401673791,1649401673812,1649401673832,1649401673852,1649401673874,1649401673892,1649401673912,1649401673934,1649401673952,1649401673976,1649401673993,1649401674014,1649401674034,1649401674053,1649401674075,1649401674093,1649401674114,1649401674135,1649401674154,1649401674175,1649401674196,1649401674216,1649401674234,1649401674254,1649401674276,1649401674296,1649401674315,1649401674336,1649401674355,1649401674378,1649401674395,1649401674416,1649401674437,1649401674456,1649401674477,1649401674496,1649401674516,1649401674540,1649401674557,1649401674580,1649401674597,1649401674617,1649401674639,1649401674658,1649401674680,1649401674698,1649401674717,1649401674739,1649401674759,1649401674780,1649401674805,1649401674818,1649401674843,1649401674860,1649401674879,1649401674901,1649401674919,1649401674939,1649401674961,1649401674980,1649401675002,1649401675020,1649401675042,1649401675060,1649401675081,1649401675101,1649401675120,1649401675144,1649401675160,1649401675181,1649401675202,1649401675221,1649401675243,1649401675261,1649401675286,1649401675304,1649401675322,1649401675342,1649401675362,1649401675382,1649401675404,1649401675422,1649401675444,1649401675463,1649401675483,1649401675504,1649401675523,1649401675544,1649401675563,1649401675583,1649401675606,1649401675624,1649401675644,1649401675664,1649401675684,1649401675711,1649401675725,1649401675745,1649401675765,1649401675785,1649401675807,1649401675825,1649401675845,1649401675867,1649401675886,1649401675907,1649401675926,1649401675947,1649401675967,1649401675986,1649401676008,1649401676027,1649401676072,1649401676074,1649401676087,1649401676108,1649401676127,1649401676148,1649401676168,1649401676188,1649401676209,1649401676228,1649401676248,1649401676269,1649401676288,1649401676310,1649401676329,1649401676349,1649401676370,1649401676389,1649401676410,1649401676430,1649401676449,1649401676471,1649401676490,1649401676511,1649401676530,1649401676550,1649401676571,1649401676590,1649401676612,1649401676631,1649401676652,1649401676671,1649401676691,1649401676713,1649401676732,1649401676751,1649401676772,1649401676792,1649401676812,1649401676832,1649401676852,1649401676874,1649401676893,1649401676914,1649401676933,1649401676953,1649401676974,1649401676993,1649401677014,1649401677034,1649401677054,1649401677075,1649401677094,1649401677114,1649401677135,1649401677154,1649401677176,1649401677195,1649401677215,1649401677235,1649401677255,1649401677276,1649401677295,1649401677316,1649401677337,1649401677356,1649401677377,1649401677397,1649401677417,1649401677436,1649401677457,1649401677478,1649401677497,1649401677517,1649401677538,1649401677557,1649401677579,1649401677599,1649401677618,1649401677639,1649401677658,1649401677679,1649401677698,1649401677718,1649401677740,1649401677758,1649401677780,1649401677799,1649401677819,1649401677840,1649401677859,1649401677881,1649401677900,1649401677920,1649401677940,1649401677960,1649401677981,1649401678002,1649401678020,1649401678042,1649401678061,1649401678082,1649401678101,1649401678121,1649401678142,1649401678161,1649401678181,1649401678203,1649401678222,1649401678243,1649401678262,1649401678284,1649401678302,1649401678322,1649401678344,1649401678362,1649401678383,1649401678405,1649401678423,1649401678445,1649401678463,1649401678483,1649401678505,1649401678524,1649401678545,1649401678564,1649401678584,1649401678604,1649401678624,1649401678646,1649401678665,1649401678685,1649401678706,1649401678725,1649401678746,1649401678766,1649401678785,1649401678806,1649401678826,1649401678847,1649401678866,1649401678886,1649401678907,1649401678926,1649401678948,1649401678967,1649401678987,1649401679007,1649401679027,1649401679048,1649401679069,1649401679088,1649401679109,1649401679128,1649401679148,1649401679169,1649401679188,1649401679210,1649401679228,1649401679249,1649401679269,1649401679290,1649401679309,1649401679329,1649401679351,1649401679370,1649401679390,1649401679411,1649401679430,1649401679452,1649401679470,1649401679490,1649401679512,1649401679532,1649401679552,1649401679571,1649401679591,1649401679613,1649401679631,1649401679652,1649401679672,1649401679693,1649401679712,1649401679732,1649401679754,1649401679772,1649401679793,1649401679814,1649401679833,1649401679854,1649401679873,1649401679893,1649401679915,1649401679934,1649401679956,1649401679974,1649401679994,1649401680015,1649401680034,1649401680054,1649401680076,1649401680095,1649401680116,1649401680135,1649401680155,1649401680176,1649401680195,1649401680217,1649401680235,1649401680256,1649401680277,1649401680296,1649401680317,1649401680336,1649401680356,1649401680378,1649401680396,1649401680418,1649401680437,1649401680459,1649401680477,1649401680497,1649401680518,1649401680539,1649401680560,1649401680578,1649401680598,1649401680620,1649401680638,1649401680658,1649401680679,1649401680699,1649401680721,1649401680739,1649401680759,1649401680781,1649401680799,1649401680819,1649401680842,1649401680861,1649401680881,1649401680900,1649401680922,1649401680940,1649401680960,1649401680982,1649401681001,1649401681022,1649401681041,1649401681061,1649401681083,1649401681101,1649401681121,1649401681142,1649401681162,1649401681182,1649401681202,1649401681223,1649401681243,1649401681263,1649401681284,1649401681303,1649401681323,1649401681345,1649401681363,1649401681384,1649401681405,1649401681425,1649401681444,1649401681464,1649401681486,1649401681504,1649401681526,1649401681544,1649401681565,1649401681585,1649401681605,1649401681625,1649401681645,1649401681665,1649401681685,1649401681705,1649401681726,1649401681746,1649401681766,1649401681786,1649401681806,1649401681826,1649401681847,1649401681867,1649401681887,1649401681907,1649401681927,1649401681947,1649401681968,1649401681988,1649401682008,1649401682028,1649401682048,1649401682068,1649401682088,1649401682108,1649401682128,1649401682148,1649401682169,1649401682189,1649401682209,1649401682229,1649401682249,1649401682269,1649401682290,1649401682310,1649401682330,1649401682352,1649401682370,1649401682392,1649401682410,1649401682431,1649401682453,1649401682471,1649401682493,1649401682511,1649401682531,1649401682553,1649401682571,1649401682592,1649401682612,1649401682632,1649401682654,1649401682672,1649401682692,1649401682714,1649401682733,1649401682753,1649401682775,1649401682793,1649401682814,1649401682834,1649401682855,1649401682874,1649401682894,1649401682915,1649401682934,1649401682956,1649401682974,1649401682994,1649401683016,1649401683035,1649401683055,1649401683075,1649401683095,1649401683116,1649401683135,1649401683157,1649401683176,1649401683196,1649401683217,1649401683236,1649401683256,1649401683278,1649401683297,1649401683318,1649401683337,1649401683358,1649401683377,1649401683397,1649401683419,1649401683437,1649401683458,1649401683478,1649401683498,1649401683519,1649401683538,1649401683558,1649401683580,1649401683599,1649401683620,1649401683639,1649401683660,1649401683679,1649401683699,1649401683721,1649401683739,1649401683761,1649401683780,1649401683800,1649401683821,1649401683840,1649401683860,1649401683882,1649401683900,1649401683921,1649401683942,1649401683961,1649401683983,1649401684001,1649401684022,1649401684042,1649401684061,1649401684082,1649401684102,1649401684124,1649401684142,1649401684162,1649401684184,1649401684203,1649401684224,1649401684243,1649401684263,1649401684285,1649401684303,1649401684324,1649401684343,1649401684364,1649401684388]
print(len(consolelist))
dertalist = []
secdertalis = []
for i in range(0,len(consolelist)-1):
    if i % 30 == 0:
        secdertalis.append(consolelist[i]-consolelist[i-30])
    dertalist.append(consolelist[i+1]-consolelist[i])


x = np.arange(0,len(consolelist)-1)
x2 = np.arange(0,len(secdertalis))
y = dertalist
y2 = secdertalis
fig = plt.figure()
plt.scatter(x,y,c = 'r')
plt.show()
# fig2 = plt.figure()
# plt.scatter(x2,y2,c = 'g')
# plt.show()