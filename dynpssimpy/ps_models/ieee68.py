def load():
    return {
        'base_mva': 100,
        'f': 60,
        'slack_bus': '16',

        'buses': [
            ['name',    'V_n'],
            ['01',      100],
            ['02',      100],
            ['03',      100],
            ['04',      100],
            ['05',      100],
            ['06',      100],
            ['07',      100],
            ['08',      100],
            ['09',      100],
            ['10',      100],
            ['11',      100],
            ['12',      100],
            ['13',      100],
            ['14',      100],
            ['15',      100],
            ['16',      100],
            ['17',      100],
            ['18',      100],
            ['19',      100],
            ['20',      100],
            ['21',      100],
            ['22',      100],
            ['23',      100],
            ['24',      100],
            ['25',      100],
            ['26',      100],
            ['27',      100],
            ['28',      100],
            ['29',      100],
            ['30',      100],
            ['31',      100],
            ['32',      100],
            ['33',      100],
            ['34',      100],
            ['35',      100],
            ['36',      100],
            ['37',      100],
            ['38',      100],
            ['39',      100],
            ['40',      100],
            ['41',      100],
            ['42',      100],
            ['43',      100],
            ['44',      100],
            ['45',      100],
            ['46',      100],
            ['47',      100],
            ['48',      100],
            ['49',      100],
            ['50',      100],
            ['51',      100],
            ['52',      100],
            ['53',      100],
            ['54',      100],
            ['55',      100],
            ['56',      100],
            ['57',      100],
            ['58',      100],
            ['59',      100],
            ['60',      100],
            ['61',      100],
            ['62',      100],
            ['63',      100],
            ['64',      100],
            ['65',      100],
            ['66',      100],
            ['67',      100],
            ['68',      100],
        ],

        'lines': [
            ['name',    'from_bus',     'to_bus',     'R',      'X',        'B',  ],  # 'length',    'unit'],
            ['L07-23',    '07',           '23',       0.0005,    0.0272,         0],       # 0,         0],
            ['L17-36',    '17',           '36',       0.0005,    0.0045,    0.3200],       # 0,         0],
            ['L18-49',    '18',           '49',       0.0076,    0.1141,    1.1600],       # 0,         0],
            ['L18-50',    '18',           '50',       0.0012,    0.0288,    2.0600],       # 0,         0],
            ['L19-68',    '19',           '68',       0.0016,    0.0195,    0.3040],       # 0,         0],
            ['L21-68',    '21',           '68',       0.0008,    0.0135,    0.2548],       # 0,         0],
            ['L22-21',    '22',           '21',       0.0008,    0.0140,    0.2565],       # 0,         0],
            ['L23-22',    '23',           '22',       0.0006,    0.0096,    0.1846],       # 0,         0],
            ['L24-23',    '24',           '23',       0.0022,    0.0350,    0.3610],       # 0,         0],
            ['L24-68',    '24',           '68',       0.0003,    0.0059,    0.0680],       # 0,         0],
            ['L25-54',    '25',           '54',       0.0070,    0.0086,    0.1460],       # 0,         0],
            ['L26-25',    '26',           '25',       0.0032,    0.0323,    0.5310],       # 0,         0],
            ['L27-37',    '27',           '37',       0.0013,    0.0173,    0.3216],       # 0,         0],
            ['L27-26',    '27',           '26',       0.0014,    0.0147,    0.2396],       # 0,         0],
            ['L28-26',    '28',           '26',       0.0043,    0.0474,    0.7802],       # 0,         0],
            ['L29-26',    '29',           '26',       0.0057,    0.0625,    1.0290],       # 0,         0],
            ['L29-28',    '29',           '28',       0.0014,    0.0151,    0.2490],       # 0,         0],
            ['L30-53',    '30',           '53',       0.0008,    0.0074,    0.4800],       # 0,         0],
            ['L30-61',    '30',           '61',       0.00095,   0.00915,   0.5800],       # 0,         0],
            ['L31-30',    '31',           '30',       0.0013,    0.0187,    0.3330],       # 0,         0],
            ['L31-53',    '31',           '53',       0.0016,    0.0163,    0.2500],       # 0,         0],
            ['L32-30',    '32',           '30',       0.0024,    0.0288,    0.4880],       # 0,         0],
            ['L33-32',    '33',           '32',       0.0008,    0.0099,    0.1680],       # 0,         0],
            ['L34-33',    '34',           '33',       0.0011,    0.0157,    0.2020],       # 0,         0],
            ['L36-34',    '36',           '34',       0.0033,    0.0111,    1.4500],       # 0,         0],
            ['L36-61',    '36',           '61',       0.0011,    0.0098,    0.6800],       # 0,         0],
            ['L37-68',    '37',           '68',       0.0007,    0.0089,    0.1342],       # 0,         0],
            ['L38-31',    '38',           '31',       0.0011,    0.0147,    0.2470],       # 0,         0],
            ['L38-33',    '38',           '33',       0.0036,    0.0444,    0.6930],       # 0,         0],
            ['L40-41',    '40',           '41',       0.0060,    0.0840,    3.1500],       # 0,         0],
            ['L40-48',    '40',           '48',       0.0020,    0.0220,    1.2800],       # 0,         0],
            ['L41-42',    '41',           '42',       0.0040,    0.0600,    2.2500],       # 0,         0],
            ['L42-18',    '42',           '18',       0.0040,    0.0600,    2.2500],       # 0,         0],
            ['L43-17',    '43',           '17',       0.0005,    0.0276,         0],       # 0,         0],
            ['L44-39',    '44',           '39',            0,    0.0411,         0],       # 0,         0],
            ['L44-43',    '44',           '43',       0.0001,    0.0011,         0],       # 0,         0],
            ['L45-35',    '45',           '35',       0.0007,    0.0175,    1.3900],       # 0,         0],
            ['L45-39',    '45',           '39',            0,    0.0839,         0],       # 0,         0],
            ['L45-44',    '45',           '44',       0.0025,    0.0730,         0],       # 0,         0],
            ['L46-38',    '46',           '38',       0.0022,    0.0284,    0.4300],       # 0,         0],
            ['L47-53',    '47',           '53',       0.0013,    0.0188,    1.3100],       # 0,         0],
            ['L48-47',    '48',           '47',       0.00125,   0.0134,    0.8000],       # 0,         0],
            ['L49-46',    '49',           '46',       0.0018,    0.0274,    0.2700],       # 0,         0],
            ['L51-45',    '51',           '45',       0.0004,    0.0105,    0.7200],       # 0,         0],
            ['L51-50',    '51',           '50',       0.0009,    0.0221,    1.6200],       # 0,         0],
            ['L52-37',    '52',           '37',       0.0007,    0.0082,    0.1319],       # 0,         0],
            ['L52-55',    '52',           '55',       0.0011,    0.0133,    0.2138],       # 0,         0],
            ['L54-53',    '54',           '53',       0.0035,    0.0411,    0.6987],       # 0,         0],
            ['L55-54',    '55',           '54',       0.0013,    0.0151,    0.2572],       # 0,         0],
            ['L56-55',    '56',           '55',       0.0013,    0.0213,    0.2214],       # 0,         0],
            ['L57-56',    '57',           '56',       0.0008,    0.0128,    0.1342],       # 0,         0],
            ['L58-57',    '58',           '57',       0.0002,    0.0026,    0.0434],       # 0,         0],
            ['L59-58',    '59',           '58',       0.0006,    0.0092,    0.1130],       # 0,         0],
            ['L60-57',    '60',           '57',       0.0008,    0.0112,    0.1476],       # 0,         0],
            ['L60-59',    '60',           '59',       0.0004,    0.0046,    0.0780],       # 0,         0],
            ['L61-60',    '61',           '60',       0.0023,    0.0363,    0.3804],       # 0,         0],
            ['L63-58',    '63',           '58',       0.0007,    0.0082,    0.1389],       # 0,         0],
            ['L63-62',    '63',           '62',       0.0004,    0.0043,    0.0729],       # 0,         0],
            ['L65-62',    '65',           '62',       0.0004,    0.0043,    0.0729],       # 0,         0],
            ['L66-56',    '66',           '56',       0.0008,    0.0129,    0.1382],       # 0,         0],
            ['L66-65',    '66',           '65',       0.0009,    0.0101,    0.1723],       # 0,         0],
            ['L67-66',    '67',           '66',       0.0018,    0.0217,    0.3660],       # 0,         0],
            ['L68-67',    '68',           '67',       0.0009,    0.0094,    0.1710],       # 0,         0],
            ['L27-53',    '27',           '53',       0.0320,    0.3200,    0.4100],       # 0,         0],
        ],

        'transformers': [
            ['name',      'from_bus',     'to_bus',      'R',       'X',         'ratio_from'],  # 'ratio_to'],  #'S_n', 'V_n_from', 'V_n_to', 'N_par'],
            #['T2-30',     '2',           '30',         1000, 345, 16.5, 1, 0, 0.181, 1 / 1.0250, 1],
            ['T01-54',    '01',           '54',            0,    0.0181,          1/1.0250],        # 0],
            ['T02-58',    '02',           '58',            0,    0.0250,          1/1.0700],        # 0],
            ['T03-62',    '03',           '62',            0,    0.0200,          1/1.0700],        # 0],
            ['T04-19',    '04',           '19',       0.0007,    0.0142,          1/1.0700],        # 0],
            ['T05-20',    '05',           '20',       0.0009,    0.0180,          1/1.0090],        # 0],
            ['T06-22',    '06',           '22',            0,    0.0143,          1/1.0250],        # 0],
            ['T08-25',    '08',           '25',       0.0006,    0.0232,          1/1.0250],        # 0],
            ['T09-29',    '09',           '29',       0.0008,    0.0156,          1/1.0250],        # 0],
            ['T10-31',    '10',           '31',            0,    0.0260,          1/1.0400],        # 0],
            ['T11-32',    '11',           '32',            0,    0.0130,          1/1.0400],        # 0],
            ['T12-36',    '12',           '36',            0,    0.0075,          1/1.0400],        # 0],
            ['T13-17',    '13',           '17',            0,    0.0033,          1/1.0400],        # 0],
            ['T14-41',    '14',           '41',            0,    0.0015,          1/1.0000],        # 0],
            ['T15-42',    '15',           '42',            0,    0.0015,          1/1.0000],        # 0],
            ['T16-18',    '16',           '18',            0,    0.0030,          1/1.0000],        # 0],
            ['T20-19',    '20',           '19',       0.0007,    0.0138,          1/1.0600],        # 0],
            ['T34-35',    '34',           '35',       0.0001,    0.0074,          1/0.9460],        # 0],
            ['T63-64',    '63',           '64',       0.0016,    0.0435,          1/1.0600],        # 0],
            ['T65-64',    '65',           '64',       0.0016,    0.0435,          1/1.0600],        # 0],
        ],

        'loads': [
            ['name',    'bus',  'P',        'Q'],
            ['17',      '17',   100*60.00,      100*3.00],
            ['18',      '18',   100*24.70,      100*1.23],
            ['19',      '19',   100*0.00,       100*0.00],
            ['20',      '20',   100*6.800,      100*1.03],
            ['21',      '21',   100*2.740,      100*1.15],
            ['22',      '22',   100*0.00,       100*0.00],
            ['23',      '23',   100*2.480,      100*0.85],
            ['24',      '24',   100*3.09,       100*-0.92],
            ['25',      '25',   100*2.24,       100*0.47],
            ['26',      '26',   100*1.39,       100*0.17],
            ['27',      '27',   100*2.810,      100*0.76],
            ['28',      '28',   100*2.060,      100*0.28],
            ['29',      '29',   100*2.840,      100*0.27],
            ['30',      '30',   100*0.00,       100*0.00],
            ['31',      '31',   100*0.00,       100*0.00],
            ['32',      '32',   100*0.00,       100*0.00],
            ['33',      '33',   100*1.12,       100*0.00],
            ['34',      '34',   100*0.00,       100*0.00],
            ['35',      '35',   100*0.00,       100*0.00],
            ['36',      '36',   100*1.02,       100*-0.1946],
            ['37',      '37',   100*0.00,       100*0.00],
            ['38',      '38',   100*0.00,       100*0.00],
            ['39',      '39',   100*2.67,       100*0.126],
            ['40',      '40',   100*0.6563,     100*0.2353],
            ['41',      '41',   100*10.00,      100*2.50],
            ['42',      '42',   100*11.50,      100*2.50],
            ['43',      '43',   100*0.00,       100*0.00],
            ['44',      '44',   100*2.6755,     100*0.0484],
            ['45',      '45',   100*2.08,       100*0.21],
            ['46',      '46',   100*1.507,      100*0.285],
            ['47',      '47',   100*2.0312,     100*0.3259],
            ['48',      '48',   100*2.4120,     100*0.022],
            ['49',      '49',   100*1.6400,     100*0.29],
            ['50',      '50',   100*1.00,       100*-1.47],
            ['51',      '51',   100*3.37,       100*-1.22],
            ['52',      '52',   100*1.58,       100*0.30],
            ['53',      '53',   100*2.527,      100*1.1856],
            ['54',      '54',   100*0.00,       100*0.00],
            ['55',      '55',   100*3.22,       100*0.02],
            ['56',      '56',   100*2.00,       100*0.736],
            ['57',      '57',   100*0.00,       100*0.00],
            ['58',      '58',   100*0.00,       100*0.00],
            ['59',      '59',   100*2.34,       100*0.84],
            ['60',      '60',   100*2.088,      100*0.708],
            ['61',      '61',   100*1.04,       100*1.25],
            ['62',      '62',   100*0.00,       100*0.00],
            ['63',      '63',   100*0.00,       100*0.00],
            ['64',      '64',   100*0.09,       100*0.88],
            ['65',      '65',   100*0.00,       100*0.00],
            ['66',      '66',   100*0.00,       100*0.00],
            ['67',      '67',   100*3.200,      100*1.5300],
            ['68',      '68',   100*3.290,      100*0.32],
        ],

        'generators': {
            'GEN': [
                ['name', 'bus',     'S_n',  'X_l',      'R_a',      'X_d',      'X_d_t',        'X_d_st',       'T_d0_t',      'T_d0_st',      'X_q',      'X_q_t',        'X_q_st',       'T_q0_t',       'T_q0_st',      'H',        'D_0',      'D_1',     'S(1.0)',       'S(1.2)',       'V_n',      'D',         'V',        'P'],
                ['01',   '01',      100,    0.0125,     0.0,        0.1,        0.031,          0.025,          10.2,           0.05,           0.069,      0.0416667,      0.025,         1.5,             0.035,          42.,        0,          0,         0,              0,              0,          4.0,        1.0450,     100*2.50],
                ['02',   '02',      100,    0.035,      0.0,        0.295,      0.0697,         0.05,           6.56,           0.05,           0.282,      0.0933333,      0.05,          1.5,             0.035,          30.2,       0,          0,         0,              0,              0,          9.75,       0.9800,     100*5.45],
                ['03',   '03',      100,    0.0304,     0.0,        0.2495,     0.0531,         0.045,          5.7,            0.05,           0.237,      0.0714286,      0.045,         1.5,             0.035,          35.8,       0,          0,         0,              0,              0,          10,         0.9830,     100*6.50],
                ['04',   '04',      100,    0.0295,     0.0,        0.262,      0.0436,         0.035,          5.69,           0.05,           0.258,      0.0585714,      0.035,         1.5,             0.035,          28.6,       0,          0,         0,              0,              0,          10,         0.9970,     100*6.32],
                ['05',   '05',      100,    0.027,      0.0,        0.33,       0.066,          0.05,           5.4,            0.05,           0.31,       0.0883333,      0.05,          0.44,            0.035,          26.,        0,          0,         0,              0,              0,          3,          1.0110,     100*5.05],
                ['06',   '06',      100,    0.0224,     0.0,        0.254,      0.05,           0.04,           7.3,            0.05,           0.241,      0.0675000,      0.04,          0.4,             0.035,          34.8,       0,          0,         0,              0,              0,          10,         1.0500,     100*7.00],
                ['07',   '07',      100,    0.0322,     0.0,        0.295,      0.049,          0.04,           5.66,           0.05,           0.292,      0.0666667,      0.04,          1.5,             0.035,          26.4,       0,          0,         0,              0,              0,          8,          1.0630,     100*5.60],
                ['08',   '08',      100,    0.028,      0.0,        0.29,       0.057,          0.045,          6.7,            0.05,           0.280,      0.0766667,      0.045,         0.41,            0.035,          24.3,       0,          0,         0,              0,              0,          9,          1.0300,     100*5.40],
                ['09',   '09',      100,    0.0298,     0.0,        0.2106,     0.057,          0.045,          4.79,           0.05,           0.205,      0.0766667,      0.045,         1.96,            0.035,          34.5,       0,          0,         0,              0,              0,          14,         1.0250,     100*8.00],
                ['10',   '10',      100,    0.0199,     0.0,        0.169,      0.0457,         0.04,           9.37,           0.05,           0.115,      0.0615385,      0.04,          1.5,             0.035,          31.0,       0,          0,         0,              0,              0,          5.56,       1.0100,     100*5.00],
                ['11',   '11',      100,    0.0103,     0.0,        0.128,      0.018,          0.012,          4.1,            0.05,           0.123,      0.0241176,      0.012,         1.5,             0.035,          28.2,       0,          0,         0,              0,              0,          13.6,       1.0000,     100*10.00],
                ['12',   '12',      100,    0.022,      0.0,        0.101,      0.031,          0.025,          7.4,            0.05,           0.095,      0.0420000,      0.025,         1.5,             0.035,          92.3,       0,          0,         0,              0,              0,          13.5,       1.0156,     100*13.50],
                ['13',   '13',      200,    0.0030,     0.0,        0.0296,     0.0055,         0.004,          5.9,            0.05,           0.0286,     0.0074000,      0.004,         1.5,             0.035,          248.0,      0,          0,         0,              0,              0,          33,         1.0110,     100*35.91],
                ['14',   '14',      100,    0.0017,     0.0,        0.018,      0.00285,        0.0023,         4.1,            0.05,           0.0173,     0.0037931,      0.0023,        1.5,             0.035,          300.0,      0,          0,         0,              0,              0,          100,        1.0000,     100*17.85],
                ['15',   '15',      100,    0.0017,     0.0,        0.018,      0.00285,        0.0023,         4.1,            0.05,           0.0173,     0.0037931,      0.0023,        1.5,             0.035,          300.0,      0,          0,         0,              0,              0,          100,        1.0000,     100*10.00],
                ['16',   '16',      200,    0.0041,     0.0,        0.0356,     0.0071,         0.0055,         7.8,            0.05,           0.0334,     0.0095000,      0.0055,        1.5,             0.035,          225.0,      0,          0,         0,              0,              0,          50,         1.0000,     100*40.00],
            ],
        },
    }

'''

% ************************ EXCITER DATA STARTS ************************
% Description of Exciter data starts
% exciter data DC4B,ST1A model
%     1 - exciter type (1 for DC4B, 0 for ST1A)
%     2 - machine number
%     3 - input filter time constant T_R
%     4 - voltage regulator gain K_A
%     5 - voltage regulator time constant T_A
%     6 - maximum voltage regulator output V_Rmax
%     7 - minimum voltage regulator output V_Rmin
%     8 - exciter constant K_E
%     9 - exciter time constant T_E
%    10 - E_1
%    11 - S(E_1)
%    12 - E_2
%    13 - S(E_2)
%    14 - stabilizer gain K_F
%    15 - stabilizer time constant T_F
%    16 - K_P
%    17 - K_I
%    18 - K_D
%    19 - T_D
exc_con = [...
    1 1  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 2  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 3  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 4  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 5  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 6  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 7  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 8  0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    0 9  0.01 200. 0.00 5.0  -5.0  0.0     0   0      0     0      0     0     0   0   0  0    0;
    1 10 0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 11 0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
    1 12 0.01 1.   0.02 10.  -10.  1.0    .785 3.9267 0.070 5.2356 0.910 0.030 1.0 200 50 50 .01;
          ];
 %************************ EXCITER DATA ENDS ************************
 
% ************************ PSS DATA STARTS ************************
%1-S. No.
%2-present machine index
%3-pssgain
%4-washout time constant
%5-first lead time constant
%6-first lag time constant
%7-second lead time constant
%8-second lag time constant
%9-third lead time constant
%10-third lag time constant
%11-maximum output limit
%12-minimum output limit
pss_con = [
    1   1   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    2   2   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    3   3   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    4   4   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    5   5   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    6   6   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    7   7   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    8   8   20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    9   9   12  10  0.09  0.02  0.09  0.02  1     1    0.2 -0.05 ;
    10  10  20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    11  11  20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    12  12  20  15  0.15  0.04  0.15  0.04  0.15  0.04 0.2 -0.05 ;
    ];
%************************ PSS DATA ENDS ************************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
'''