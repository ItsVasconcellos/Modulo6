var directions = {
    left: {
      linear: { x: 0.0, y: 0.0, z: 0.0 },
      angular: { x: 0.0, y: 0.0, z: 0.5 },
    },
    right: {
      linear: { x: 0.0, y: 0.0, z: 0.0 },
      angular: { x: 0.0, y: 0.0, z: -0.5 },
    },
    up: {
      linear: { x: 0.5, y: 0.0, z: 0.0 },
      angular: { x: 0.0, y: 0.0, z: 0.0 },
    },
    down: {
      linear: { x: -0.5, y: 0.0, z: 0.0 },
      angular: { x: 0.0, y: 0.0, z: 0.0 },
    },
  };

  var ros = new ROSLIB.Ros({
    url: "ws://localhost:9090",
  });

  ros.on("connection", function () {
    console.log("Connected to websocket server.");
  });

  ros.on("error", function (error) {
    console.log("Error connecting to websocket server: ", error);
  });

  ros.on("close", function () {
    console.log("Connection to websocket server closed.");
  });

  // Topic to receive video frames
  var videoTopic = new ROSLIB.Topic({
    ros: ros,
    name: "/video_frames",
    messageType: "sensor_msgs/CompressedImage",
  });

  var messageTimestamps = { current: [] };

  // Function to handle incoming video frames
  videoTopic.subscribe(function (message) {
    var img = document.getElementById("videoStream");
    img.src = "data:image/jpeg;base64," + message.data;
    messageTimestamps.current.push(Date.now());
    // Remove timestamps older than one second
    const oneSecondAgo = Date.now() - 1000;
    messageTimestamps.current = messageTimestamps.current.filter(
      (timestamp) => timestamp >= oneSecondAgo
    );
    // Calculate FPS as the number of messages received in the last second
    var fps = messageTimestamps.current.length;
    var fpsElement = document.getElementById("fps");
    fpsElement.innerHTML = "FPS: " + fps;
  });

  var velocityTopic = new ROSLIB.Topic({
    ros: ros,
    name: "/velocity",
    messageType: "geometry_msgs/Twist",
  });

  velocityTopic.publish();

  var killRobotService = new ROSLIB.Service({
    ros: ros,
    name: "/kill_robot",
    serviceType: "std_srvs/Trigger",
  });

  window.onload = function () {
    videoTopic.subscribe();
  };
  function funcao() {
    var request = new ROSLIB.ServiceRequest({});

    killRobotService.callService(request, function (result) {
      console.log(
        "Result for service call on " +
          killRobotService.name +
          ": " +
          result.message
      );
      if (result.success) {
        alert("Robot killed successfully");
      } else {
        alert("Failed to kill the robot");
      }
    });
  }