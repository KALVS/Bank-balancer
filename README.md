# Bank balancer
So my partner and I had a look at our joint bills account and realised we had made some extra curricular purchases.

This neat little python script will read an ING statement, check if the transaction is unexpected and create a neat little CSV of all the times you've used the wrong card. This is really helpful since I can now prove how much we've spent on decor, homewares and rubix cube oil.

You'll need to modify the expectedPurchases array to fit your own, but yea, enjoy. Please don't steal my bank account.

You can also look into generating a PDF or a HTML with the DF or just using the print statements like I did,

# Usage
Standard Python script...

0. Download some ING bank statements, put them into a folder, update the directoryPath variable
1. cd to project root
2. pip install -r requirements.txt
3. Populate expected expenses into the array. for example: expectedTransactions = ['Rent', 'Anytime Fitness', 'SPOTIFY', 'GWW']
4. python main.py
5. ?????
6. Savings
