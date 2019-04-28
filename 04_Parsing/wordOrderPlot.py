import sys
import matplotlib.pyplot as plt

labels = {0:'bas', 1:'bre', 2:'cat', 3:'dan', 4:'eng', 5:'hin-eng', 6:'hin', 7:'fre', 8:'gre', 9:'ser', 10:'slo', 11:'uyg'}
x = [0.85, 0.10, 0.30, 0.05, 0.03, 0.54, 0.75, 0.12, 0.17, 0.12, 0.35, 1.0]  # proportion of OV
y = [0.15, 0.90, 0.70, 0.95, 0.97, 0.46, 0.25, 0.88, 0.83, 0.88, 0.65, 0]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
plt.savefig(sys.argv[1])
plt.show()


"""
Word Orders (from wordOrterTests)

Basque
Object Before Verb: 0.8532801418439716
Verb Before Object: 0.14671985815602837
Breton
Object Before Verb: 0.10178117048346055
Verb Before Object: 0.8982188295165394
Catalan
Object Before Verb: 0.2994726138361311
Verb Before Object: 0.7005273861638689
Danish
Object Before Verb: 0.05383647798742138
Verb Before Object: 0.9461635220125786
English
Object Before Verb: 0.03019175846593227
Verb Before Object: 0.9698082415340677
Hindi English
Object Before Verb: 0.5406283856988082
Verb Before Object: 0.4593716143011918
Hindi
Object Before Verb: 0.7471889468655839
Verb Before Object: 0.2528110531344161
French
Object Before Verb: 0.11801632140615191
Verb Before Object: 0.8819836785938481
Greek
Object Before Verb: 0.16555082166768106
Verb Before Object: 0.8344491783323189
Serbian
Object Before Verb: 0.12352684417285029
Verb Before Object: 0.8764731558271497
Slovak
Object Before Verb: 0.35295283392786364
Verb Before Object: 0.6470471660721363
Uyghur
Object Before Verb: 0.9991496598639455
Verb Before Object: 0.0008503401360544217
"""
