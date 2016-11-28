library(MASS)
library(BAS)
data(UScrime)
UScrime[,-2] <- log(UScrime[,-2])
crime.ZS <- bas.lm(y~.,
                   data = UScrime,
                   prior = "ZS-null",
                   modelprior = uniform(),
                   method = "MCMC")
diagnostics(crime.ZS)
plot(crime.ZS, which = 1, add.smooth = F)
plot(crime.ZS, which = 2, add.smooth = F)
plot(crime.ZS, which = 3)
plot(crime.ZS, which = 4)

image(crime.ZS, rotate = F)

