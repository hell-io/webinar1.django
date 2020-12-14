CREATE TABLE "external".letters (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	country text NOT NULL,
	address text NOT NULL,
	"content" text NOT NULL,
	sender_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"timestamp" timestamptz NOT NULL DEFAULT now(),
	CONSTRAINT letters_pkey PRIMARY KEY (id)
);

INSERT INTO "external".letters (id,country,address,"content",sender_id,"timestamp") VALUES
	 ('e4b07cb6-9bcb-4610-8f7b-1f4dfa195e72','Russia','Moscow, Souyznaya, 5, 13','Самый лучший Дедушка Мороз, меня зовут Мария. Мне 7 годиков. Можешь привезти мне шахматы, телефон сенсорный с чехлом для него и босоножки. А еще маме самый красивый браслет из золота с бриллиантами. И папе, а у папы есть мама. Он и так самый счастливый. Я обещаю также продолжать слушаться родителей, учиться на одни пятерки. Подарив нам все это, ты сделаешь мир немного счастливей. Желаю тебе всего самого наилучшего, особенно неугасаемой любви, щедрости, доброты и сил. С любовью, Мария!','5709de29-92f1-4de3-b333-1d0ad301b136','2020-12-13 01:58:54.688002+03'),
	 ('068bcd5d-89b5-4a11-8984-8fcaa44d91b9','Russia','Kazan, Lenina, 14','Здравствуй, Дедушка Мороз! Пишет тебе Оля. Мне 9 лет. Спасибо тебе за подарки, которые ты приносил мне раньше. Я люблю рисовать и играть в настольные игры. Мечтаю получить набор фломастеров с блестками. Обещаю быть послушной девочкой целый год. С нетерпением жду встречи с тобой.','d41210fc-64f3-4be9-bb08-1a1475e991a1','2020-12-13 01:58:54.688002+03'),
	 ('ce97c6fc-ac19-42f5-b8e5-9a610da804d0','Norway','Bergen, Bryggesporden, 88','Enhver har rett til beskyttelse av de åndelige og materielle interesser som er et resultat av ethvert vitenskapelig, litterært eller kunstnerisk verk som han har skapt.','25b061c3-62e5-4b3d-b4c8-279c356e6501','2020-12-13 01:58:54.688002+03'),
	 ('ebe9e75e-4301-44d5-83ff-36f4806ec2e1','Britain','Westwood St, 6','Every Christmas I''m a very good boy put out milk and cookies for this guy to enjoyBut Santa never brings the right toy felt like giving up on all this holiday joy','5d6b9e61-0aca-42fb-b208-5c41364a2476','2020-12-13 01:58:54.688002+03'),
	 ('e9e9861c-08c5-4391-9614-ae388747144f','Norway','Oslo, Apotekergata, 7','Undervisningen skal ta sikte på å utvikle den menneskelige personlighet og styrke respekten for menneskerettighetene og de grunnleggende friheter. Den skal fremme forståelse, toleranse og vennskap mellom alle nasjoner og rasegrupper eller religiøse grupper og skal støtte De Forente Nasjoners arbeid for å opprettholde fred.','e9d31b06-c268-4061-8c8a-ccb6982a9623','2020-12-13 01:58:54.688002+03');

INSERT INTO operational.behavior_records (id,"action",child_id) VALUES
	 ('df09ba65-ef60-42e1-b304-15c419f26c37','хватала кошку за хвост','deef0ff4-6241-4def-b60b-3a7e678e4ca0'),
	 ('53e6ebf6-36e5-42b8-a0d5-d42a4b0d31a6','читал младшему брату на ночь','b44e6443-a64a-4f51-9741-6b3339e3f9ac');

 INSERT INTO operational.children (id,external_id,"name") VALUES
	 ('59acf5e4-4d16-424c-a669-cb9b46e6d47b','5709de29-92f1-4de3-b333-1d0ad301b136','Masha'),
	 ('7bbfd136-9fcb-4ae2-a6b9-f4360fefec62','d41210fc-64f3-4be9-bb08-1a1475e991a1','Danny'),
	 ('deef0ff4-6241-4def-b60b-3a7e678e4ca0','25b061c3-62e5-4b3d-b4c8-279c356e6501','Olya'),
	 ('b44e6443-a64a-4f51-9741-6b3339e3f9ac','5d6b9e61-0aca-42fb-b208-5c41364a2476','Sven'),
	 ('f824e500-8cd7-4baa-8fb0-25946e98069e','e9d31b06-c268-4061-8c8a-ccb6982a9623','Ingrid');