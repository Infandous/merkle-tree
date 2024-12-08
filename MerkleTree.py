from hashlib import sha256

class MerkleTree(object):
    def __init__(self):
        pass

    #function to yield n number of transactions
    def chunks(self, transaction, n):
        for i in range(0, len(transaction), n):
            yield transaction[i:i+n]

    #recursive function to build Merkle Tree
    def merkle_tree(self, transactions):
        #base case
        if len(transactions)==1:
            return sha256(transactions[0].encode('utf-8')).hexdigest()

        sub_tree = []
        for i in self.chunks(transactions, 2):
            if (len(i)==2): #even case
                hash = sha256((i[0]+i[1]).encode('utf-8')).hexdigest()
            else: #odd case
                hash = sha256((i[0]+i[0]).encode('utf-8')).hexdigest()
            sub_tree.append(hash)

        
        return self.merkle_tree(sub_tree)


if __name__ =='__main__':
    mk = MerkleTree()
    merkle_hash = mk.merkle_tree(["TX1", "TX2", "TX3", "TX4", "TX5", "TX6"])
    print(merkle_hash)
