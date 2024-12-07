# Smart-Wallet-Tracking
The following is a library of functions useful for blockchain analysis with python 🐍 and optionally, SQL. This library has tools for hash normalization, heuristic clustering, developing cluster balances, and many more to come. I plan on posting my research results in the "notebooks" file to give a feel for how this library can be used for blockchain analysis. In the future, I plan on:

- Making the SQL portion more generalizable.
- Give parser an option to parse directly to a SQL database with a predefined schema.
- Significantly abstracting away the details by creating master functions. This will make the library far easier to learn.
- Add different clustering heuristics such as temporal clustering.
- Brush up unit tests and post them to the tests file.

The psuedonymity of the Bitcoin blockchain may provide insight into the behaviors of successful traders. Although several methods exist to further anonymize one's transactions, many also exist to do the opposite. Techniques from blockchain forensics and analysis can potentially be used to develop signals and/or filters from a wallet cluster's trading activities. This project is an application of these techniques, with the end goal of identifying some edge hidden within the network. If Bitcoin trader's alpha can be reverse engineered from this public data, it suggests that there is significant alpha decay risk in the bitcoin markets. This would mean that Bitcoin trading necessiates anonymization - an additional fixed cost. This could potentially impact a Bitcoin strategies position on the risk curve.
