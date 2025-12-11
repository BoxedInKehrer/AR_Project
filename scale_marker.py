import trimesh

mesh = trimesh.load("meshes/aruco_marker_100.ply")
mesh.apply_scale(0.5)
mesh.export("aruco_marker_100_small.ply")
