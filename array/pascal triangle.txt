Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

solution:

class Solution {
    public List<List<Integer>> generate(int numRows) {
        int j;
        List<List<Integer>> pas = new ArrayList<>();
        if(numRows<1) return pas;
        List<Integer> temp=new ArrayList<>();
        temp.add(1);
        pas.add(temp);
        if(numRows==1) return pas;
        for(int i=2;i<=numRows;i++){
            temp=new ArrayList<>();
            temp.add(1);
            j=1;
            while(i>2 && j<pas.get(i-2).size()){
                temp.add(pas.get(i-2).get(j) + pas.get(i-2).get(j-1));
                j++;
            }
            temp.add(1);
            pas.add(temp);
        }
        return pas;
    }
}