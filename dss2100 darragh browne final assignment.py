{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "fish_data = pd.read_csv('C:/Users/35385/Pictures/2020-01/New folder/gandhi_et_al_bouts.csv', skiprows = 4) #import data and remove first four lines of meta data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "bout_length_wt = fish_data[fish_data.genotype == 'wt'].bout_length #selecting only wild type fish from the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "bout_length_mut = fish_data[fish_data.genotype == 'mut'].bout_length #selecting only mutant type fish from the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == '__main__':\n",
    "    def bootstrap_replicate(data, func, size=1):                  #generates bootstrap replicate\n",
    "        bootstrap_sample = np.random.choice(data, len(data))\n",
    "        return func(bootstrap_sample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "#compute the mean active bout lengths of both groups\n",
    "mean_wt = np.mean(bout_length_wt)\n",
    "mean_mut = np.mean(bout_length_mut)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Creates bootstrap replicates using bootstrap_replicate function\n",
    "bootstrap_wt = bootstrap_replicate(bout_length_wt, np.mean, size =1000)\n",
    "bootstrap_mut = bootstrap_replicate(bout_length_mut, np.mean, size = 1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "#computes 95% confidence intervals\n",
    "conf_int_wt = np.percentile(bootstrap_wt, [2.5, 97.5])\n",
    "conf_int_mut = np.percentile(bootstrap_mut, [2.5, 97.5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Wild Type Fish: mean length = 3.874 , confidence interval = [3.8, 3.8]\n",
      "Mutant Fish: mean length = 6.543 , confidence interval = [6.5, 6.5] \n",
      "\n"
     ]
    }
   ],
   "source": [
    "#print the results of the above tests\n",
    "print(\"\"\"\n",
    "Wild Type Fish: mean length = {0:.3f} , confidence interval = [{1:.1f}, {2:.1f}]\n",
    "Mutant Fish: mean length = {3:.3f} , confidence interval = [{4:.1f}, {5:.1f}] \n",
    "\"\"\". format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
