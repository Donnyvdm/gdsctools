


"""

library("Hmisc")
  2 
  3 # obs and pred need to be numeric for all functions!
  4 
  5 # function to calculate the concordance index
  6 cIDX <- function(pred, obs) {
  7   # calculate the concordance index 
  8   rcorr.cens(pred, obs)[1]
  9 }
 10 
"""


xtrain_obs = """909712   753597   905958   909762   949177   910401   925342   753555 
0.010738 0.009982 0.002121 0.005834 0.002038 0.007406 0.002127 0.002503 
  687814   907789   924244   908143   907172   753563   910566   907274 
0.006738 0.002075 0.003968 0.003934 0.011618 0.003489 0.003282 0.003439 
  753533   684681   909974   684055   907279   687804   753611   906869 
0.006339 0.037917 0.003866 0.069795 0.012368 0.088955 0.022956 0.003986 
  924246   910688   688121   910692   924248   946367   949164   906763 
0.000906 0.002092 0.010744 0.003798 0.042295 0.016578 0.017666 0.160514 
  910546   905974   724866   924110 
0.005039 0.012676 0.007170 0.002117""".split()




xTrain_pred = """
               s0        s19         s39          s59           s69
909712 0.02062554 0.01667454 0.017952263  0.017788310  0.0175772377
753597 0.02062554 0.01667454 0.014480282  0.011683907  0.0110985122
905958 0.02062554 0.01667454 0.001847579 -0.015769078 -0.0180257622
909762 0.02062554 0.01667454 0.008597932  0.004827847  0.0047242928
949177 0.02062554 0.01667454 0.015778650  0.019695281  0.0194995181
910401 0.02062554 0.01667454 0.015778650  0.020146465  0.0211882398
925342 0.02062554 0.01667454 0.015778650  0.020146465  0.0211882398
753555 0.02062554 0.01667454 0.017952263  0.002009810 -0.0003729716
687814 0.02062554 0.01667454 0.011882255 -0.017938860 -0.0221408265
907789 0.02062554 0.01667454 0.015778650  0.015599545  0.0158813436
924244 0.02062554 0.01667454 0.009642239  0.003447087  0.0018895132
908143 0.02062554 0.01667454 0.015778650  0.016853723  0.0128634632
907172 0.02062554 0.01667454 0.010205919  0.008282756  0.0084487187
753563 0.02062554 0.01667454 0.008597932  0.004827847  0.0046568035
910566 0.02062554 0.01667454 0.017952263  0.024049895  0.0250195314
907274 0.02062554 0.01667454 0.015778650  0.004174827  0.0023074987
753533 0.02062554 0.01667454 0.028682700  0.033030274  0.0337273176
684681 0.02062554 0.01667454 0.004135912 -0.008038419  0.0036305902
909974 0.02062554 0.01667454 0.030856313  0.036933705  0.0374911199
684055 0.02062554 0.01667454 0.015778650  0.016145546  0.0154642319
907279 0.02062554 0.01667454 0.017952263  0.016220234  0.0164806604
687804 0.02062554 0.01667454 0.015778650  0.013433696  0.0121247138
753611 0.02062554 0.01667454 0.015778650  0.016060173  0.0164759670
906869 0.02062554 0.01667454 0.012906920  0.013366774  0.0140699299
924246 0.02062554 0.01667454 0.015778650  0.016060173  0.0164084777
910688 0.02062554 0.01667454 0.015778650  0.020146465  0.0211207505
688121 0.02062554 0.01667454 0.017952263  0.025595804  0.0266409471
910692 0.02062554 0.01667454 0.015778650  0.014210844  0.0142633627
924248 0.02062554 0.01667454 0.015778650  0.020146465  0.0211207505
946367 0.02062554 0.01667454 0.015307035 -0.001399759 -0.0047136414
949164 0.02062554 0.01667454 0.015778650  0.020146465  0.0211882398
906763 0.02062554 0.01667454 0.020568325  0.028637504  0.0304219119
910546 0.02062554 0.01667454 0.014098852  0.010175801  0.0106098967
905974 0.02062554 0.01667454 0.012379532  0.012186186  0.0122125210
724866 0.02062554 0.01667454 0.009708642 -0.004585214 -0.0060123688
924110 0.02062554 0.01667454 0.014480282  0.015770198  0.0158107850
                 s79
909712  0.0172798444
753597  0.0105851368
905958 -0.0188211900
909762  0.0049350022
949177  0.0194521274
910401  0.0217212440
925342  0.0217212440
753555 -0.0014778941
687814 -0.0238544536
907789  0.0168513665
924244  0.0002805226
908143  0.0097963704
907172  0.0087853038
753563  0.0046605593
910566  0.0254601718
907274  0.0015127746
753533  0.0341541266
684681  0.0088156781
909974  0.0376186115
684055  0.0152182139
907279  0.0165400601
687804  0.0115462430
753611  0.0166972216
906869  0.0147057453
924246  0.0164227786
910688  0.0214468010
688121  0.0269412812
910692  0.0144322996
924248  0.0214468010
946367 -0.0054855306
949164  0.0217212440
906763  0.0310792909
910546  0.0109404837
905974  0.0122497886
724866 -0.0064051420
924110  0.0156091591
"""

results = [0.5 ,  0.5 , 0.5150794 , 0.5126984 , 0.5111111 , 0.5222222 ]



xtrain_obs = """0.010738 0.009982 0.002121 0.005834 0.002038 0.007406 0.002127 0.002503
0.006738 0.002075 0.003968 0.003934 0.011618 0.003489 0.003282 0.003439
0.006339 0.037917 0.003866 0.069795 0.012368 0.088955 0.022956 0.003986
0.000906 0.002092 0.010744 0.003798 0.042295 0.016578 0.017666 0.160514
0.005039 0.012676 0.007170 0.002117""".split()
xtrain_obs = [str(x) for x in xtrain_obs]


v1 =  """0.0172798444  0.0105851368 -0.0188211900  0.0049350022  0.0194521274
 0.0217212440  0.0217212440 -0.0014778941 -0.0238544536  0.0168513665
 0.0002805226  0.0097963704  0.0087853038  0.0046605593  0.0254601718
 0.0015127746  0.0341541266  0.0088156781  0.0376186115  0.0152182139
 0.0165400601  0.0115462430  0.0166972216  0.0147057453  0.0164227786
 0.0214468010  0.0269412812  0.0144322996  0.0214468010 -0.0054855306
 0.0217212440  0.0310792909  0.0109404837  0.0122497886 -0.0064051420
 0.0156091591""".split()
v1 = [float(x) for x in v1]

#def test_v1():
#    cindex = corr.cens(v1, xtrain_obs)

