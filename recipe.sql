/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - recipe
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`recipe` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `recipe`;

/*Table structure for table `store` */

DROP TABLE IF EXISTS `store`;

CREATE TABLE `store` (
  `storeid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `post` varchar(10) DEFAULT NULL,
  `pin` varchar(10) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `logid` int(11) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`storeid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `store` */

insert  into `store`(`storeid`,`name`,`latitude`,`longitude`,`post`,`pin`,`email`,`phone`,`logid`,`status`) values (1,'Ajfan ','11.12','75.15','Kozhikode','673601','ajfan@gmail.com','9876543211',7,'approved'),(2,'Bean Bazar','11.11','12.12','Kozhikode ','673611','bean@gmail.com','9666332566',8,'pending');

/*Table structure for table `storevegitems` */

DROP TABLE IF EXISTS `storevegitems`;

CREATE TABLE `storevegitems` (
  `svid` int(11) NOT NULL AUTO_INCREMENT,
  `slogid` int(11) DEFAULT NULL,
  `vegid` int(11) DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`svid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `storevegitems` */

insert  into `storevegitems`(`svid`,`slogid`,`vegid`,`price`) values (1,8,3,10),(2,7,4,15);

/*Table structure for table `tbl_complaint` */

DROP TABLE IF EXISTS `tbl_complaint`;

CREATE TABLE `tbl_complaint` (
  `comp_id` int(30) NOT NULL AUTO_INCREMENT,
  `user_id` int(30) NOT NULL,
  `complaint` varchar(500) NOT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_complaint` */

insert  into `tbl_complaint`(`comp_id`,`user_id`,`complaint`,`reply`,`date`,`status`) values (1,1,'dissatisfied','why?','2019-05-20','pending'),(2,2,'add more recipes','definitly','2019-05-21','replied'),(3,1,'follow another method for making veg kuruma','definitely','2019-05-27','pending');

/*Table structure for table `tbl_feedback` */

DROP TABLE IF EXISTS `tbl_feedback`;

CREATE TABLE `tbl_feedback` (
  `feedback_id` int(30) NOT NULL AUTO_INCREMENT,
  `reg_id` int(30) NOT NULL,
  `feedback` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_feedback` */

insert  into `tbl_feedback`(`feedback_id`,`reg_id`,`feedback`,`date`,`status`) values (1,1,'Nice app','2019-05-20','seen'),(2,2,'good','2019-05-21','seen');

/*Table structure for table `tbl_ingredients` */

DROP TABLE IF EXISTS `tbl_ingredients`;

CREATE TABLE `tbl_ingredients` (
  `reci_id` int(30) NOT NULL,
  `veg_id` int(30) NOT NULL,
  `serial_no` int(30) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_ingredients` */

insert  into `tbl_ingredients`(`reci_id`,`veg_id`,`serial_no`) values (1,1,1),(1,2,2),(1,3,3),(1,4,5),(1,5,6),(1,6,7),(1,8,8),(1,10,10),(1,11,12),(1,12,13),(1,14,14),(2,2,17),(2,3,18),(2,4,19),(2,5,20),(2,6,21),(2,12,22),(2,14,23),(3,2,24),(3,6,25),(3,9,26),(4,2,27),(4,6,28),(4,7,29),(5,2,30),(5,3,31),(5,6,32),(6,1,33),(6,5,34),(6,2,35),(6,3,36),(6,6,37),(7,2,38),(7,8,39),(7,6,40),(8,2,41),(8,3,42),(8,6,43),(9,10,44),(9,2,45),(10,1,46),(10,2,47),(10,6,48),(10,8,49);

/*Table structure for table `tbl_login` */

DROP TABLE IF EXISTS `tbl_login`;

CREATE TABLE `tbl_login` (
  `uname` varchar(45) NOT NULL,
  `password` varchar(40) NOT NULL,
  `type` varchar(30) NOT NULL,
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_login` */

insert  into `tbl_login`(`uname`,`password`,`type`,`loginid`) values ('admin','admin','admin',1),('hasbeenahasbi20@gmail.com','011235','user',2),('hasbeenahasbi20@gmail.com','011235','user',3),('hasbeenahasbi20@gmail.com','011235','user',4),('reju84@gmail.com','12345','user',5),('shanooba@gmail.com','12789','user',6),('ajfan@gmail.com','123','store',7),('bean@gmail.com','123','store',8),('likh@g.com','123','user',9);

/*Table structure for table `tbl_recipe` */

DROP TABLE IF EXISTS `tbl_recipe`;

CREATE TABLE `tbl_recipe` (
  `reci_id` int(30) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `how_to_make` varchar(5000) NOT NULL,
  `type` varchar(30) NOT NULL,
  `author_id` int(30) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`reci_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_recipe` */

insert  into `tbl_recipe`(`reci_id`,`name`,`description`,`how_to_make`,`type`,`author_id`,`photo`,`status`) values (1,'Sambar','Kerala sambar is a delicious variety of sambar made with mix veggies,lentils,roasted spices and coconut is one of the highlight of this sambar recipe.','\r\nWash dal several times and pressure cook with 2 cups water for 4 whistles. The dal needs to be cooked till smooth.While the dal cooks, dry roast the ingredients under \"to roast and powder\".roast coriander seeds till they smell good, dals to golden, and then red chilies to crisp and methi seeds till they begin to smell good. Cool these and powdered.Wash and chop the veggies.\r\nAdd 5 cups of water to a pot, add the chopped veggies and cook until soft.When the water turns slightly hot, transfer about Â¼ cup hot water with a ladle to a separate bowl and soak tamarind in it.\r\nWhen the pressure goes off, mash the dal to smooth. The dal needs to be very smooth otherwise it doesnâ€™t taste good.When the vegetables are completely cooked, add sambhar powder and salt. Cook for 3 to 5 minutes.Pour the tamarind pulp, filtered if you desire.Add smooth dal, mix well to blend the dal with water. Bring it to a boil. Check if there is enough salt and sourness. If needed add more. Add coriander leaves and stir.\r\nMeanwhile, heat another pan with oil or ghee.Add mustard cumin and methi. When they begin to sizzle, add curry leaves, broken red chili. When the leaves turn crisp, off the heat add hing.Pour this seasoning to the sambar. Stir well. Simmer for 2 to 3 minutes for the sambar to become flavorful.','admin',0,'/static/recipe/sambar.jpg','approved'),(2,'Avial','Avial is a traditional South Indian dish, popular in Kerala, Tamilnadu and Karnataka cuisines. It is a delicious mix of a variety of vegetables cooked with coconut. It is also an essential dish in Kerala Sadya, a grand vegetarian feast on banana leaves, prepared during festivals like Onam and vishu and also for special occasions.','Clean/ peel and wash all the vegetables. Cut into 2 inch long pieces. Slice the onions. Boil/ cook the yam, cucumber, ash gourd, plantain, carrot in Â¾ glass water for about five minutes. Add other vegetables, onion, curry leaves, one slit green chili and cover and cook till tender (It should be tender and slightly crisp).Add salt and toss the vegetables. Grind the coconut coarsely with garlic, green chili, small onion, turmeric, jeerah and curry leaves. Add this mix to the cooked vegetables, combine well, then cover and cook for some more time. Add the curd and mix well.Adjust the salt and switch off the flame. Pour 1 tbsp Coconut oil for seasoning and mix well. Serve hot with rice. ','admin',0,'/static/recipe/avial.jpg','approved'),(3,'cabbage thoran','Cabbage Thoran is a very tasty  thoran. It is a great side dish for rice.','Soak Cherupayar in water for 3 hours. Pressure cook the payar with just enough water to cover payar (no salt). Keep aside. Chop the cabbage into fine strands. Grind coarsely Coconut, chilly, few curry leaves, onion and turmeric. Heat oil in a kadai, pop mustards, then curry leaves and add the cabbage, salt. Mix well and cover and cook the cabbage. Once it is cooked, add the cooked Cherupayar and the ground coconut mix. Donâ€™t stir or mix, just cover and cook for another two minutes. Finally mix all together well by folding in. There your healthy thoran is ready to be served.','admin',0,'/static/recipe/cabbage thoran.jpg','approved'),(4,'Beetroot pachadi','Beetroot Pachadi is a chutney style dish of beetroot which is an integral part of Onam sadya. It is quite easy to make and goes well with steamed rice.','Ingredients:\r\nBeetroot - 1 grated.\r\nGreen chilly - 1 cut in large size\r\nYogurt \r\nOil\r\nMustard\r\nTurmeric powder\r\nChilly powder\r\nSalt\r\nWater\r\n\r\nPreparation:\r\nTake a beetroot grate it and keep aside. Heat a pan pour oil to it. Add mustard . Add green chillies and beetroot to the oil fry it in oil till the beetroot is cooked . Add salt, turmeric powder, chilly powder to it and mix well . And beetroot uppari is ready.\r\nRemove the pan from the gas and allow the beetroot to be cool.Take required amount of yogurt in a bowl. Add the cooked beetroot to it and mix well.','admin',0,'/static/recipe/2019_05_17_13_51_47.001177.jpg','approved'),(5,'carrot thoran','Carrot Thoran or Carrot Upperi is a tasty and healthy Kerala style vegetable preparation.It is an essential part of Onam or Vishu sadya, keralites feasts.','Combine grated coconut with turmeric powder, green chilies, and cumin powder. Set aside until ready to use.Heat 2 or 3 tsp coconut oil over medium heat. Splutter mustard seeds and fry dried red chilies and curry leaves. Add carrot, finely chopped onion, salt and grated coconut mix. Mix well. Cook covered for 4 â€“ 5 minutes. Open the lid and stir for a few minutes until completely dry (do not overcook).Serve with rice.','admin',0,'/static/recipe/2019_05_17_14_07_25.340413.jpg','approved'),(6,'veg kuruma','Vegetable Kuruma is a delicious, very popular restaurant  recipe in South India. Vegetable Kuruma  is a stew of assorted veggies simmered in a thick spicy coconut based gravy which pairs well with Parotta ,Poori,Chappathi, Appam and Idiyappam.','\r\nGrind all the Grinding ingredients with little water to a smooth paste.Cut the vegetables into medium sized piece.Cook all the chopped vegetables with little water and salt to taste or you can pressure cook the vegetables for 1 whistle and open it after 5 minutes.If the pressure has not subsided, you can pour little water on top or show it on the running water, off the cooker to release the pressure and then open it.Heat oil in a pan, add cinnamon, curry leaves, chopped onions and fry until onions become translucent.Now add chopped tomatoes and saute for few seconds now add all the cooked vegetables and add little water to it, cook for 5 mins.Add the grounded coconut paste and fry for another 5-8 min until all the raw smell goes. Garnish with coriander leaves. Serve hot with Appam, Noolappam and other.','admin',0,'/static/recipe/2019_05_17_14_59_40.256424.jpg','approved'),(7,'Puliyinchi','Puliyinchi is a combination of tamarind and ginger with some jaggiri added in order to counter the spiciness of ginger. It is used as pickle.','Heat some oil in a clay pot, and add mustard. When they start sputtering add curry leaves and dry red chillies (vattal mulaku) pieces, stir well. To this add items under 1 (ginger, small onion and green chillies) and salt, continue stirring till its color turns brown. Add items under 3 (chilli powder and turmeric powder) to this mixture, stir well. Mix tamarind water and salt with this and stir well. In the end, add jaggiri mixture (item number 5). Allow the preparation to cool.','admin',0,'/static/recipe/2019_05_21_11_42_42.919561.jpg','approved'),(8,'Chilli potato','A popular indian street food recipe which is prepared with potato wedges and spicy asian suace.','firstly, peel the skin of potatoes and chop them to thick pieces.further, boil the potato pieces for 2 minutes adding little salt.Further, mix corn flour and crushed pepper to boiled potatoes.','user',2,'/static/recipe/chilli potato.jpg','approved'),(9,'Brinjal fry','Brinjal is also called as eggplant. Brinjal is high in water content and potassium. Brinjal can be made in several different ways and here is the most quick, easy and tasty Brinjal Fry recipe.','Wash the brinjal and cut into small round pieces. Heat oil in a pan and stir fry brinjal pieces over medium high heat for 2-3 minutes.Mix salt and remaining spices and now cook them on a low heat. Brinjals turns soft very quickly, so no need to stir again and again. Leave to cook for about 2 minutes.','admin',0,'/static/recipe/2019_05_27_11_12_47.138636.jpg','approved'),(10,'Tomato curry','Tomatoes are different from other vegetables. They can be sour yet blend very well spices and other veggies.','Heat oil in a pan. Put in mustard seeds. Let them crackle. Add broken red chillies and curry leaves. Saute for 5 seconds. Add chopped ginger, garlic, onions, and hing powder. Continue sauteing till onions become golden. Lower the heat. Add turmeric powder,red chilli powder, and coriander powder. Saute for five seconds. Add in chopped tomatoes. Add salt. Increase the heat. Mix well. Cover the pan and cook while stirring at intervals. Add some water to keep it wet. Cook them till they become mushy. Turn off the fire. Tomato Curry is ready to serve.','user',1,'/static/recipe/2019_05_27_11_39_25.926044.jpg','pending');

/*Table structure for table `tbl_user` */

DROP TABLE IF EXISTS `tbl_user`;

CREATE TABLE `tbl_user` (
  `Reg_id` int(30) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `house_nm` varchar(50) NOT NULL,
  `street` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `pin` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `phone_no` bigint(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`Reg_id`),
  UNIQUE KEY `Reg_id` (`Reg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_user` */

insert  into `tbl_user`(`Reg_id`,`name`,`house_nm`,`street`,`district`,`pin`,`gender`,`phone_no`,`email`) values (1,'Hasbi','Parammal','chettippadi','676319','malappuram','Female',9526674891,'hasbeenahasbi20@gmail.com'),(2,'Rejina','chaithram','calicut','694678','Calicut','Female',9400412359,'reju84@gmail.com'),(3,'Shanooba','Athurangatt','Ramanattukara','673633','Calicut','Female',7893451234,'shanooba@gmail.com'),(4,'Likhil','h','s','d','673611','Female',9747360170,'lik@g.com'),(5,'Likhil','h','s','d','673611','Female',9747360170,'likh@g.com');

/*Table structure for table `tbl_vegetables` */

DROP TABLE IF EXISTS `tbl_vegetables`;

CREATE TABLE `tbl_vegetables` (
  `veg_id` int(30) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  PRIMARY KEY (`veg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_vegetables` */

insert  into `tbl_vegetables`(`veg_id`,`name`,`description`) values (1,'tomato','Edible veg and berry.'),(2,'chilli','Small and spicy.'),(4,'potato','It is a plant and also the potato grows within the grownd.'),(5,'onion','The onion also known as the bulb onion or common onion, is a vegetable.'),(6,'curry leaves','It is a natural flavouring agent in various currys.'),(7,'beetroot','Taproot portion of a beet plant.'),(8,'ginger','Ginger is a flowering plant.'),(9,'cabbage','It is a leafy blue,red or white biennial plant.'),(10,'brinjal','Brinjal is a plant species in the nightshade family solanaceae and purple color edible vegetable.'),(11,'ladies Finger','It is type of green vegetable,long finger like,having a small tip at the taporing end.'),(12,'pumpkin','Pumpkin is one of the widely grown vegetables incredibly rich in vital antioxidants, and vitamins.'),(13,'mango','Mango is the star fruit of spring. Its tangy flavour compliments the weather beautifully.Once you taste it, you wont be able to stop eating'),(14,'green banana','These  are incredibly tasty and easy to eat.they are rich in many essential vitamins and minerals.');

/*Table structure for table `tbl_vegimage` */

DROP TABLE IF EXISTS `tbl_vegimage`;

CREATE TABLE `tbl_vegimage` (
  `image_id` int(30) NOT NULL AUTO_INCREMENT,
  `veg_id` int(30) NOT NULL,
  `path` varchar(100) NOT NULL,
  PRIMARY KEY (`image_id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_vegimage` */

insert  into `tbl_vegimage`(`image_id`,`veg_id`,`path`) values (1,1,'/static/veg_photos/2019_05_15_14_04_16.420844.jpg'),(2,1,'/static/veg_photos/2019_05_15_14_04_26.178883.jpg'),(3,1,'/static/veg_photos/2019_05_15_14_04_36.144459.jpg'),(4,1,'/static/veg_photos/2019_05_15_14_04_45.139546.jpg'),(5,1,'/static/veg_photos/2019_05_15_14_04_57.517602.jpg'),(6,2,'/static/veg_photos/2019_05_15_14_05_42.437865.jpg'),(7,2,'/static/veg_photos/2019_05_15_14_05_59.902188.jpg'),(8,2,'/static/veg_photos/2019_05_15_14_06_14.632770.jpg'),(9,2,'/static/veg_photos/2019_05_15_14_06_28.727590.jpg'),(10,2,'/static/veg_photos/2019_05_15_14_06_46.958783.jpg'),(11,3,'/static/veg_photos/2019_05_15_14_07_45.046666.jpg'),(12,3,'/static/veg_photos/2019_05_15_14_07_55.613678.jpg'),(13,3,'/static/veg_photos/2019_05_15_14_08_04.290906.jpg'),(14,3,'/static/veg_photos/2019_05_15_14_08_15.835157.jpg'),(15,3,'/static/veg_photos/2019_05_15_14_08_31.840592.jpg'),(16,4,'/static/veg_photos/2019_05_15_14_09_15.693352.jpg'),(17,4,'/static/veg_photos/2019_05_15_14_09_22.890180.jpg'),(18,4,'/static/veg_photos/2019_05_15_14_09_32.543975.jpg'),(19,4,'/static/veg_photos/2019_05_15_14_09_44.986893.jpg'),(20,4,'/static/veg_photos/2019_05_15_14_09_56.288890.jpg'),(21,5,'/static/veg_photos/2019_05_15_14_10_24.946010.jpg'),(22,5,'/static/veg_photos/2019_05_15_14_10_34.687189.jpg'),(23,5,'/static/veg_photos/2019_05_15_14_10_44.716222.jpg'),(24,5,'/static/veg_photos/2019_05_15_14_10_56.975569.jpg'),(25,5,'/static/veg_photos/2019_05_15_14_11_08.047799.jpg'),(26,6,'/static/veg_photos/2019_05_15_14_11_54.367684.jpg'),(27,6,'/static/veg_photos/2019_05_15_14_12_12.943993.jpg'),(28,6,'/static/veg_photos/2019_05_15_14_12_25.533289.jpg'),(29,6,'/static/veg_photos/2019_05_15_14_12_42.347669.jpg'),(30,6,'/static/veg_photos/2019_05_15_14_13_06.086995.jpg'),(31,7,'/static/veg_photos/2019_05_15_14_13_49.264598.jpg'),(32,7,'/static/veg_photos/2019_05_15_14_14_04.835211.jpg'),(33,7,'/static/veg_photos/2019_05_15_14_14_16.636463.jpg'),(34,7,'/static/veg_photos/2019_05_15_14_14_25.181909.jpg'),(35,7,'/static/veg_photos/2019_05_15_14_14_43.612305.jpg'),(36,8,'/static/veg_photos/2019_05_15_14_15_13.151881.jpg'),(37,8,'/static/veg_photos/2019_05_15_14_15_26.383604.jpg'),(38,8,'/static/veg_photos/2019_05_15_14_15_36.658173.jpg'),(39,8,'/static/veg_photos/2019_05_15_14_15_49.315567.jpg'),(40,8,'/static/veg_photos/2019_05_15_14_16_01.650579.jpg'),(41,9,'/static/veg_photos/2019_05_15_14_16_25.867879.jpg'),(42,9,'/static/veg_photos/2019_05_15_14_16_35.379375.jpg'),(43,9,'/static/veg_photos/2019_05_15_14_16_46.304414.jpg'),(44,9,'/static/veg_photos/2019_05_15_14_16_58.090603.jpg'),(45,9,'/static/veg_photos/2019_05_15_14_17_12.837906.jpg'),(46,9,'/static/veg_photos/2019_05_15_14_17_31.693292.jpg'),(47,10,'/static/veg_photos/2019_05_15_14_18_02.292281.jpg'),(48,10,'/static/veg_photos/2019_05_15_14_18_10.696049.jpg'),(49,10,'/static/veg_photos/2019_05_15_14_18_22.210405.jpg'),(50,10,'/static/veg_photos/2019_05_15_14_18_31.933172.jpg'),(51,10,'/static/veg_photos/2019_05_15_14_18_49.452187.jpg'),(52,11,'/static/veg_photos/2019_05_15_14_19_25.620357.jpg'),(53,11,'/static/veg_photos/2019_05_15_14_19_35.253242.jpg'),(54,11,'/static/veg_photos/2019_05_15_14_19_51.495370.jpg'),(55,11,'/static/veg_photos/2019_05_15_14_20_03.344539.jpg'),(56,11,'/static/veg_photos/2019_05_15_14_20_37.744329.jpg'),(57,12,'/static/veg_photos/2019_05_15_14_24_34.720466.jpg'),(58,12,'/static/veg_photos/2019_05_15_14_24_44.392617.jpg'),(59,12,'/static/veg_photos/2019_05_15_14_24_53.633478.jpg'),(60,12,'/static/veg_photos/2019_05_15_14_25_01.117391.jpg'),(61,12,'/static/veg_photos/2019_05_15_14_25_56.001855.jpg'),(62,14,'/static/veg_photos/2019_05_15_14_42_42.713458.jpg'),(63,14,'/static/veg_photos/2019_05_15_14_42_55.074388.jpg'),(64,14,'/static/veg_photos/2019_05_15_14_43_05.371622.jpg'),(65,14,'/static/veg_photos/2019_05_15_14_43_15.199211.jpg'),(66,14,'/static/veg_photos/2019_05_15_14_43_28.946642.jpg'),(67,1,'/static/veg_photos/2019_06_05_14_22_26.462008.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
