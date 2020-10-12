public class Point {
    public int x;
    public int y;
    
    public Point(int x1, int y1) {
        x = x1;
        y = y1;
    }
    
    public static Point operator+ (Point a, Point b) {
        Point result = new Point(0, 0);
        result.x = a.x + b.x;
        result.y = a.y + b.y;
        return result;
    }
    
    public override string ToString() {
        return $"({x}, {y})";
    }
    
    public override bool Equals(Object obj) {
        Point b = (Point) obj;
        if(x == b.x && y == b.y) return true;
        else return false;
    }
}

int manhattan(Point a, Point b) {
    return Math.Abs(b.x - a.x) + Math.Abs(b.y - a.y);
}

int flr(string directions) {
    Point start = new Point(0, 0);
    Point current = start;
    var faces = new List<int>{0, 1, 2, 3};
    var initHead = 0;
    var head = initHead;
    
    foreach(var i in directions) {
        if(i == 'F') {
            if(head == 0) current += new Point(0, 1);
            else if(head == 1) current += new Point(1, 0);
            else if(head == 2) current += new Point(0, -1);
            else current += new Point(-1, 0);
        }
        else if(i == 'L') {
            head = (4 + head - 1) % 4;
        }
        else if(i == 'R') {
            head = (head + 1) % 4;
        }
    }
    
    var moveCount = 0;
    while(!current.Equals(start)) {
        var possibleMoves = new List<Point>();
        possibleMoves.Add(current + new Point(0, 1));
        possibleMoves.Add(current + new Point(1, 0));
        possibleMoves.Add(current + new Point(0, -1));
        possibleMoves.Add(current + new Point(-1, 0));
        
        var leastDist = 9999;
        var nextHead = -1;
        for(int i = 0; i < possibleMoves.Count; i++) {
            var dist = manhattan(possibleMoves[i], start);
            if(dist < leastDist) {
                leastDist = dist;
                nextHead = i;
            }
        }
        current = possibleMoves[nextHead];
        while(head != nextHead) {
            if(head < nextHead) {
                head += 1;
            }
            else head -= 1;
            moveCount += 1;
        }
        moveCount += 1;
    }
    return moveCount;
}
