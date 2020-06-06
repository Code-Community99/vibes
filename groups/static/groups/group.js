function nodecreator(media_name ,poster_name, new_post) {
  // get the main  div object
  var maindiv = document.getElementById("allposts");
  // create the main div
  var mydiv = document.createElement("div");
  mydiv.setAttribute("class" , "singlepost");

  var myparagh = document.createElement("p");
  myparagh.setAttribute("class" , "profile");
  var myimg = document.createElement("img");
  myimg.setAttribute("src" , "/media/"+media_name);

  myotherdiv = document.createElement("div");
  myotherdiv.setAttribute("class" , "singlepost-info")
  myotherdiv.innerHTML = new_post;
  myparagh.appendChild(myimg);
  mydiv.appendChild(myparagh);
  mydiv.appendChild(myotherdiv);
  maindiv.appendChild(mydiv);
}
