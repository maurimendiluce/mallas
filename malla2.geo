//malla no estructurada

tm = 0.1;
tmr = 0.01;

Point(1) = {0, 0, 0, tm};
Point(2) = {1, 0, 0, tm};
Point(3) = {1, 1, 0, tm};
Point(4) = {0, 1, 0, tmr};


Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Curve Loop(1) = {1, 2, 3, 4};

Plane Surface(1) = {1};

Physical Surface("Mi superficie") = {1};

Mesh 2;

Mesh.SurfaceFaces = 1;
Mesh.Points = 1;

Save "malla_unif.msh";