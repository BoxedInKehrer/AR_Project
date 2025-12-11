## Camera to see all markers
cameraTopMiddle(world): { pose: [0.0, 0.0, 2.3, 0, -1, 0.0, 0], shape: marker, size: [0.1], focalLength: 0.895, width: 1280, height: 720, zRange: [0.5, 100] }


## markers
### corners
aruco100: {
  X: [-0.45, 0.05, 0.655, 0, 0, 0, 1],
  shape: mesh,
  mesh: <../meshes/aruco_marker_100.ply>
}
aruco101: {
  X: [ 0.45, 0.05, 0.655, 0, 0, 0, 1],
  shape: mesh,
  mesh: <../meshes/aruco_marker_100.ply>
}
aruco102: {
  X: [-0.45, 1.45, 0.655, 0, 0, 0, 1],
  shape: mesh,
  mesh: <../meshes/aruco_marker_100.ply>
}
aruco103: {
  X: [ 0.45, 1.45, 0.655, 0, 0, 0, 1],
  shape: mesh,
  mesh: <../meshes/aruco_marker_100.ply>
}

goal_marker: {
  X: [ 0, 1.25, 0.655, 0, 0, 0, 1],
  shape: mesh,
  mesh: <../meshes/aruco_marker_100.ply>
}


## objects
disc: {
  pose: [0.2, 0.2, 0.66],
  shape: cylinder,
  size: [0.02, 0.05],
  color: [1, 1, 1],
  contact: 1,
  friction: 0.1,
  mass: 0.1
}
disc_marker (disc): {
  shape: mesh,
  mesh: <../meshes/aruco_marker_100_small.ply>,
  size: [0.045],
  Q: [0.0, 0.0, 0.0125, 0.0, 0.0, 0.0, 1]
}


cue: {
  shape: box,
  size: [0.3, 0.05, 0.05],
  pose: [-0.2, 0.2, 0.67],
  color: [0.8, 0.8, 0.8],
  contact: 1,
  friction: 0.1,
  mass: 0.1
}

cue_marker (cue): {
  shape: mesh,
  mesh: <../meshes/aruco_marker_100_small.ply>,
  size: [0.045],
  Q: [0.0, 0.0, 0.026, 0.0, 0.0, 0.0, 1]
}

cue_front (cue): {
  shape: ssBox,
  size: [0.01, 0.2, 0.05, 0.0],
  Q: [0.1525, 0.0, 0.0,   0.0, 0.0, 0.0, 1],
  color: [0.8, 0.8, 0.8],
  contact: 1,
  friction: 0.1,
  mass: 0.1
}

### court boundaries
plank_front: {
  shape: box,
  size: [1.0, 0.01, 0.04],
  pose: [0, 1.5, 0.67],
  color: [0.8, 0.8, 0.8],
  contact: 1
}

plank_back: {
  shape: box,
  size: [1.0, 0.01, 0.04],
  pose: [0, 0.0, 0.67],
  color: [0.8, 0.8, 0.8],
  contact: 1
}

plank_left: {
  shape: box,
  size: [0.01, 1.5, 0.04],
  pose: [0.5, 0.75, 0.67],
  color: [0.8, 0.8, 0.8],
  contact: 1
}

plank_right: {
  shape: box,
  size: [0.01, 1.5, 0.04],
  pose: [-0.5, 0.75, 0.67],
  color: [0.8, 0.8, 0.8],
  contact: 1
}
