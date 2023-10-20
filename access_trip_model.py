import pandas as pd 
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models 
from biogeme.expressions import Beta

df = pd.read_csv('ACCESS_TRIP_MODEL_DATA.csv')
database = db.Database('accesstrip', df)

globals().update(database.variables)

#PARAMETERS TO BE ESTIMATED
ASC_CAR = Beta('ASC_CAR', 0, None, None, 0)
ASC_BUS = Beta('ASC_BUS', 0, None, None, 0)
ASC_RICKSHAW = Beta('ASC_RICKSHAW', 0, None, None, 0)
ASC_TW = Beta('ASC_TW', 0, None, None, 0)
ASC_CYCLE = Beta('ASC_CYCLE', 0, None, None, 0)
ASC_WALK = Beta('ASC_WALK', 0, None, None, 1)

B_COST = Beta('B_COST', 0, None, None, 0)

# B1_CAR = Beta('B1_CAR', 0, None, None, 0)
# B1_BUS = Beta('B1_BUS', 0, None, None, 0)
# B1_RICKSHAW = Beta('B1_RICKSHAW', 0, None, None, 0)
# B1_TW = Beta('B1_TW', 0, None, None, 0)
# B1_CYCLE = Beta('B1_CYCLE', 0, None, None, 0)
# B1_WALK = Beta('B1_WALK', 0, None, None, 1)

# B2_CAR = Beta('B2_CAR', 0, None, None, 0)
# B2_BUS = Beta('B2_BUS', 0, None, None, 0)
# B2_RICKSHAW = Beta('B2_RICKSHAW', 0, None, None, 0)
# B2_TW = Beta('B2_TW', 0, None, None, 0)
# B2_CYCLE = Beta('B2_CYCLE', 0, None, None, 0)
# B2_WALK = Beta('B2_WALK', 0, None, None, 1)

# B3_CAR = Beta('B3_CAR', 0, None, None, 0)
# B3_BUS = Beta('B3_BUS', 0, None, None, 0)
# B3_RICKSHAW = Beta('B3_RICKSHAW', 0, None, None, 0)
# B3_TW = Beta('B3_TW', 0, None, None, 0)
# B3_CYCLE = Beta('B3_CYCLE', 0, None, None, 0)
# B3_WALK = Beta('B3_WALK', 0, None, None, 1)

# B4_CAR = Beta('B4_CAR', 0, None, None, 0)
# B4_BUS = Beta('B4_BUS', 0, None, None, 0)
# B4_RICKSHAW = Beta('B4_RICKSHAW', 0, None, None, 0)
# B4_TW = Beta('B4_TW', 0, None, None, 0)
# B4_CYCLE = Beta('B4_CYCLE', 0, None, None, 0)
# B4_WALK = Beta('B4_WALK', 0, None, None, 1)

# B5_CAR = Beta('B5_CAR', 0, None, None, 0)
# B5_BUS = Beta('B5_BUS', 0, None, None, 0)
# B5_RICKSHAW = Beta('B5_RICKSHAW', 0, None, None, 0)
# B5_TW = Beta('B5_TW', 0, None, None, 0)
# B5_CYCLE = Beta('B5_CYCLE', 0, None, None, 0)
# B5_WALK = Beta('B5_WALK', 0, None, None, 1)

B6_CAR = Beta('B6_CAR', 0, None, None, 0)
B6_BUS = Beta('B6_BUS', 0, None, None, 0)
B6_RICKSHAW = Beta('B6_RICKSHAW', 0, None, None, 0)
B6_TW = Beta('B6_TW', 0, None, None, 0)
B6_CYCLE = Beta('B6_CYCLE', 0, None, None, 0)
B6_WALK = Beta('B6_WALK', 0, None, None, 1)

B7_CAR = Beta('B7_CAR', 0, None, None, 0)
B7_BUS = Beta('B7_BUS', 0, None, None, 0)
B7_RICKSHAW = Beta('B7_RICKSHAW', 0, None, None, 0)
B7_TW = Beta('B7_TW', 0, None, None, 0)
B7_CYCLE = Beta('B7_CYCLE', 0, None, None, 0)
B7_WALK = Beta('B7_WALK', 0, None, None, 1)

# B8_CAR = Beta('B8_CAR', 0, None, None, 0)
# B8_BUS = Beta('B8_BUS', 0, None, None, 0)
# B8_RICKSHAW = Beta('B8_RICKSHAW', 0, None, None, 0)
# B8_TW = Beta('B8_TW', 0, None, None, 0)
# B8_CYCLE = Beta('B8_CYCLE', 0, None, None, 0)
# B8_WALK = Beta('B8_WALK', 0, None, None, 1)

# B9_CAR = Beta('B9_CAR', 0, None, None, 0)
# B9_BUS = Beta('B9_BUS', 0, None, None, 0)
# B9_RICKSHAW = Beta('B9_RICKSHAW', 0, None, None, 0)
# B9_TW = Beta('B9_TW', 0, None, None, 0)
# B9_CYCLE = Beta('B9_CYCLE', 0, None, None, 0)
# B9_WALK = Beta('B9_WALK', 0, None, None, 1)

# B10_CAR = Beta('B10_CAR', 0, None, None, 0)
# B10_BUS = Beta('B10_BUS', 0, None, None, 0)
# B10_RICKSHAW = Beta('B10_RICKSHAW', 0, None, None, 0)
# B10_TW = Beta('B10_TW', 0, None, None, 0)
# B10_CYCLE = Beta('B10_CYCLE', 0, None, None, 0)
# B10_WALK = Beta('B10_WALK', 0, None, None, 1)

# B11_CAR = Beta('B11_CAR', 0, None, None, 0)
# B11_BUS = Beta('B11_BUS', 0, None, None, 0)
# B11_RICKSHAW = Beta('B11_RICKSHAW', 0, None, None, 0)
# B11_TW = Beta('B11_TW', 0, None, None, 0)
# B11_CYCLE = Beta('B11_CYCLE', 0, None, None, 0)
# B11_WALK = Beta('B11_WALK', 0, None, None, 1)

# B12_CAR = Beta('B12_CAR', 0, None, None, 0)
# B12_BUS = Beta('B12_BUS', 0, None, None, 0)
# B12_RICKSHAW = Beta('B12_RICKSHAW', 0, None, None, 0)
# B12_TW = Beta('B12_TW', 0, None, None, 0)
# B12_CYCLE = Beta('B12_CYCLE', 0, None, None, 0)
# B12_WALK = Beta('B12_WALK', 0, None, None, 1)

# B13_CAR = Beta('B13_CAR', 0, None, None, 0)
# B13_BUS = Beta('B13_BUS', 0, None, None, 0)
# B13_RICKSHAW = Beta('B13_RICKSHAW', 0, None, None, 0)
# B13_TW = Beta('B13_TW', 0, None, None, 0)
# B13_CYCLE = Beta('B13_CYCLE', 0, None, None, 0)
# B13_WALK = Beta('B13_WALK', 0, None, None, 1)

# B14_CAR = Beta('B14_CAR', 0, None, None, 0)
# B14_BUS = Beta('B14_BUS', 0, None, None, 0)
# B14_RICKSHAW = Beta('B14_RICKSHAW', 0, None, None, 0)
# B14_TW = Beta('B14_TW', 0, None, None, 0)
# B14_CYCLE = Beta('B14_CYCLE', 0, None, None, 0)
# B14_WALK = Beta('B14_WALK', 0, None, None, 1)

B15_CAR = Beta('B15_CAR', 0, None, None, 0)
B15_BUS = Beta('B15_BUS', 0, None, None, 0)
B15_RICKSHAW = Beta('B15_RICKSHAW', 0, None, None, 0)
B15_TW = Beta('B15_TW', 0, None, None, 0)
B15_CYCLE = Beta('B15_CYCLE', 0, None, None, 0)
B15_WALK = Beta('B15_WALK', 0, None, None, 1)

#UTILITY FUNCTION DEFINITIONS
V1 = ASC_CAR + B_COST * CAR_TC_SCALED + B6_CAR * MALE + B7_CAR * AGE + B15_CAR * HOUSEHOLD_INCOME_SCALED
V2 = ASC_BUS + B_COST * BUS_TC_SCALED + B6_BUS * MALE + B7_BUS * AGE + B15_BUS * HOUSEHOLD_INCOME_SCALED
V3 = ASC_RICKSHAW + B_COST * RICKSHAW_TC_SCALED + B6_RICKSHAW * MALE + B7_RICKSHAW * AGE + B15_RICKSHAW * HOUSEHOLD_INCOME_SCALED
V4 = ASC_TW + B_COST * TW_TC_SCALED + B6_TW * MALE + B7_TW * AGE + B15_TW * HOUSEHOLD_INCOME_SCALED
V5 = ASC_CYCLE + B_COST * CYCLE_TC_SCALED + B6_CYCLE * MALE + B7_CYCLE * AGE + B15_CYCLE * HOUSEHOLD_INCOME_SCALED
V6 = ASC_WALK + B_COST * WALK_TC_SCALED + B6_WALK * MALE + B7_WALK * AGE + B15_WALK * HOUSEHOLD_INCOME_SCALED

V = {1: V1, 2: V2, 3: V3, 4: V4, 5: V5, 6: V6}

# av = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

logprob = models.loglogit(V, None, MODE_CHOICE)

biogeme = bio.BIOGEME(database, logprob)
biogeme.modelName = 'accessTripModel-3'

results = biogeme.estimate()

pandasResults = results.getEstimatedParameters()
print(pandasResults)