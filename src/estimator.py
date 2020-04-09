#challenge 1
    
def estimator():
    print()
    print("name: 'Africa'")
    print("avgAge: 19.7")
    print("avgDailyIncomeInUSD: 5")
    print("avgDailyIncomePopulation: 0.71")
    print("periodType: 'days'")
    print("timeToElapse: 58")
    print("reportedCases: 674")
    print("population: 66622705")
    print("totalHospitalBeds: 1380614")
    print()
    print()
    print("Assignent 1")
    print("data=674")
    print("reportedCases=data")
    print("currentlyInfectedCases= reportedCases*10")
    print("severeInfectedCases= currentlyInfectedCases*50")
    data=674
    reportedCases=data
    currentlyInfectedCases = reportedCases*10
    severeInfectedCases= currentlyInfectedCases*50
    
    
    if reportedCases == data:
        Impact= (currentlyInfectedCases*(2**9))
        severeImpact= (severeInfectedCases*(2**9))        

        print()
        print()
        print("Assignment 2")
        print("severeCasesByRequestedTime= (172544000*0.15)")
        print("hospitalBed = (0.65*1380614)")
        print("BedAvailable = (1380614 - (hospitalBed))")
        print("totalHospitalBeds = BedAvailable")
        infectionsByRequestedTime = (172544000*0.15)
        severeCasesByRequestedTime= infectionsByRequestedTime
        hospitalBed = (0.65*1380614)
        BedAvailable = (1380614 - (hospitalBed))
        if infectionsByRequestedTime == (172544000*0.15):
            severeCasesByRequestedTime= infectionsByRequestedTime
            hospitalBedsByRequestedTime = BedAvailable
            print()
            print()
            print("Assignment 3")            
            print("infectionsByRequestedTime= (172544000*0.15)")
            print("infectionsByRequestedTime2 = (172544000*0.02)")
            print("dollarsInFlightaday=1.5")
            print("dollarsInFlightIn30Days= 1.5*30")
            infectionsByRequestedTime = (172544000*0.15)
            infectionsByRequestedTime2 = (172544000*0.02)
            dollarsInFlightaday=1.5
            dollarsInFlightIn30Days= 1.5*30
            if infectionsByRequestedTime == (172544000*0.15):
                casesForICUByRequestedTime = infectionsByRequestedTime
                casesForVentilatorsByRequestedTime = infectionsByRequestedTime2
                moneyLikelyTobeLossInDollars = round((infectionsByRequestedTime*0.65*dollarsInFlightIn30Days),2)

                print()
                print()
                print("Output are")
                return {("data =", data),
                        ("Impact =", Impact),
                        ("severeImpact =", severeImpact),
                        ("severeCasesByRequestedTime =", severeCasesByRequestedTime),
                        ("hospitalBedsByRequestedTime =", hospitalBedsByRequestedTime),
                        ("casesForICUByRequestedTime=",casesForICUByRequestedTime),
                        ("casesForVentilatorsByRequestedTime=", casesForVentilatorsByRequestedTime),
                        ("moneyLikelyTobeLossInDollars=", moneyLikelyTobeLossInDollars)}




    
        
