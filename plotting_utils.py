import numpy as np
import matplotlib.pyplot as plt

def moving_average(Xs, Ys, n_bins):
    Xs_bin = np.linspace(min(Xs), max(Xs), n_bins)
    
    Ys_bin = []
    List = []
    print(Xs_bin)
    for i in range(len(Xs_bin) - 1):
        boolean_List = (Xs >= Xs_bin[i]) & (Xs <= Xs_bin[i+1])
        print(sum(boolean_List))
        List.append((Xs_bin[i] + Xs_bin[i+1])/2)
        y_bin = [y for y, b in zip(Ys, boolean_List) if b]
        Ys_bin.append(np.mean(y_bin))
        
    
    return List, Ys_bin   

def barplot_with_CI(Xs, Ys):
    x_unique = np.sort(RS_summary['n_hidden_layers'].unique())
    
    y_mean = []
    y_CI = []
    
    for x in x_unique:
        boolean_List = Xs == x
        y_List = [x for x, b in zip(Ys, boolean_List) if b]
        
        y_mean.append(np.mean(y_List))
        y_CI.append(1.96 * np.std(y_List)/ math.sqrt(len(y_List)))
    
    x_pos = [x for x in range(len(x_unique))]
    
    fig, ax = plt.subplots()
    ax.bar(x_pos, y_mean, align='center', alpha=0.5, ecolor='black')
    ax.errorbar(x=x_pos, y=y_mean, yerr=y_CI, label='95% CI', fmt='ko')
    
    return ax