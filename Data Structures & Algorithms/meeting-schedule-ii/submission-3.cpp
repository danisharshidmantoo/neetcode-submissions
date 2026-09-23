/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<int>start;
        vector<int>End;
        for(auto interval:intervals){
            start.push_back(interval.start);
            End.push_back(interval.end);
        }
        sort(start.begin(),start.end());
        sort(End.begin(),End.end());
        int res = 0;
        int count = 0;
        int s = 0;
        int e = 0;
        while(s<intervals.size()){
            if(start[s]<End[e]){
                s += 1;
                count += 1;
            }
            else{
                e += 1;
                count -= 1;
            }
            res = max(res,count);
        }
    return res;}
};
