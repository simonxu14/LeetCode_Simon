import java.util.ArrayList;
import java.util.List;

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> courses = new ArrayList<List<Integer>>();
        for (int i = 0; i < numCourses; i++) {
        	courses.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < prerequisites.length; i++) {
        	courses.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }
        int[] track = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
        	if (dfs(courses, i, track) == false)
        		return false;
        }
        return true
    }
    
    public boolean dfs(List<List<Integer>> courses, int start, int[] track)
    {
    	if (track[start] == 2)
    		return true;
    	if (track[start] == 1)
    		return false;
    	track[start] = 1;
    	for (int j = 0; j < courses.get(start).size(); j++) {
    		if (dfs(courses, courses.get(start).get(j), track) == false)
    			return false;
    	}
    	track[start] = 2;
    	return true;
    }
}