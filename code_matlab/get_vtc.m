function [tau] = get_vtc(r, v, a, vt1, vt2)
    % Get time to contact at a specific segment (of the boundary) 
    % Params:
    %   r: instant position (rx, ry) of the CoP 
    %   v: instant velocity (vx, vy) of the CoP
    %   a: instant velocity (ax, ay) of the CoP
    %   vt1: 1st vertex (x, y) of the boundary segment
    %   vt2: 2nd vertex (x, y) of the boundary segment
    % Returns:
    %   tau: time to contact at an instant time (s)
    
    A_VERY_LARGE_NUMBER = 999;

    tau = A_VERY_LARGE_NUMBER;

    rx = r(1);
    ry = r(2);
    vx = v(1);
    vy = v(2);
    ax = a(1);
    ay = a(2);
    x1 = vt1(1);
    y1 = vt1(2);
    x2 = vt2(1);
    y2 = vt2(2);

    if x2 == x1 
        A = ax/2;
        B = vx;
        C = rx - x1;
    else
        s = (y2 - y1)/(x2 - x1);
        A = (ay - s*ax)/2;
        B = (vy - s*vx);
        C = ((ry - y1) - s*(rx - x1));        
    end

    p = [A B C];
    rts = roots(p);
    for j = 1: length(rts)
        if (rts(j) > 0) && (isreal(rts(j)) == 1)
            if tau > rts(j)
                tau = rts(j);
            end
        end
    end
end