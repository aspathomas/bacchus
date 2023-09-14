CREATE TABLE users
(
    id SERIAL PRIMARY key,
    uuid VARCHAR(100),
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(255),
    mdp VARCHAR(255),
    is_admin bool
);

CREATE TABLE wine
(
    id SERIAL PRIMARY key,
    nom VARCHAR(100),
    region VARCHAR(100),
    couleur VARCHAR(100),
    description text,
    prix_moyen INT,
    est_petillant bool
);

create table note
(
    id SERIAL PRIMARY key,
    user_id INT,
    wine_id INT,
    note INT,
   	CONSTRAINT fk_user
      FOREIGN KEY(user_id) 
	  REFERENCES users(id),
	CONSTRAINT fk_wine
      FOREIGN KEY(wine_id)
	  REFERENCES wine(id)
);

create table commentaire
(
    id SERIAL PRIMARY key,
    user_id INT,
    wine_id INT,
    commentaire text,
   	CONSTRAINT fk_user
      FOREIGN KEY(user_id) 
	  REFERENCES users(id),
	CONSTRAINT fk_wine
      FOREIGN KEY(wine_id)
	  REFERENCES wine(id)
);