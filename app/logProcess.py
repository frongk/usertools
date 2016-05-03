#!\var\www\html\userfind\flask\bin\python2.7
import pandas as pd
import time
import sys

def timeConvert(t_in):
#    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t_in))
    t1 = time.strftime('%H', time.gmtime(t_in))
    return int(t1)

def parseLog():
    with open('log','r') as f:
        lines = f.readlines()

    timeStamps = []; userT = []; text = []
    badLines = 0
    for mess in lines:
        try:
            cols = mess.split('\t',3)
            text.append(cols[2].rstrip())
            userT.append(cols[1])
            timeStamps.append(timeConvert(int(cols[0])))

        except:
            badLines = badLines + 1
            continue

    df = pd.DataFrame({'TimeStamps' : timeStamps,
                       'user'       : userT,
                       'message'    : text })

    return df


def plotGen(df_in,user_in):
#    alpha_1 = 0.3
#    vCounts.plot(kind = 'bar', alpha = alpha_1)
#    sns.countplot(x="TimeStamps", data=df_in[df.user == 'fr4nk'], palette = "PuBuGn_d", alpha = 0.8)
    if user_in == 'all':
        #sns.countplot(x="TimeStamps", data=df_in, palette = "PuBuGn_d", alpha = 0.8)
        tester = df_in.TimeStamps.value_counts(sort=False).sort_index()
        return tester
    elif df_in[df_in.user == user_in].empty:
        return 'this user doesn\'t like to chat'
    else:
        #sns.countplot(x="TimeStamps", data=df_in[df_in.user == user_in], palette = "PuBuGn_d", alpha = 0.8)
        tester = df_in[df_in.user == user_in].TimeStamps.value_counts(sort=False).sort_index()
        return tester

def visjsOut(tbct):
    idxL = tbct.index.tolist()
    valL = tbct.tolist()
    return idxL, valL

def index_max(values):
    return max(xrange(len(values)),key=values.__getitem__)

def mainlog(user):
    df = parseLog()
    out1 = plotGen(df,user)
    if not isinstance(out1,str):
        x, y = visjsOut(out1)
        return x, y, user, index_max(y), sum(y)
    else:
        return out1,"reach out to this person",user,"N/A","N/A"

if __name__ == '__main__':
    output01 = mainlog(sys.argv[1])
    print output01
