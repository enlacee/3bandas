-- phpMyAdmin SQL Dump
-- version 3.2.4
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 10-12-2012 a las 03:36:13
-- Versión del servidor: 5.1.41
-- Versión de PHP: 5.3.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `bandas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'developer'),
(2, 'administrator');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=61 ;

--
-- Volcar la base de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add log entry', 7, 'add_logentry'),
(20, 'Can change log entry', 7, 'change_logentry'),
(21, 'Can delete log entry', 7, 'delete_logentry'),
(22, 'Can add persona', 8, 'add_persona'),
(23, 'Can change persona', 8, 'change_persona'),
(24, 'Can delete persona', 8, 'delete_persona'),
(25, 'Can add jugador', 9, 'add_jugador'),
(26, 'Can change jugador', 9, 'change_jugador'),
(27, 'Can delete jugador', 9, 'delete_jugador'),
(28, 'Can add pais', 10, 'add_pais'),
(29, 'Can change pais', 10, 'change_pais'),
(30, 'Can delete pais', 10, 'delete_pais'),
(31, 'Can add torneo', 11, 'add_torneo'),
(32, 'Can change torneo', 11, 'change_torneo'),
(33, 'Can delete torneo', 11, 'delete_torneo'),
(34, 'Can add categoria juego', 12, 'add_categoriajuego'),
(35, 'Can change categoria juego', 12, 'change_categoriajuego'),
(36, 'Can delete categoria juego', 12, 'delete_categoriajuego'),
(37, 'Can add estados', 13, 'add_estados'),
(38, 'Can change estados', 13, 'change_estados'),
(39, 'Can delete estados', 13, 'delete_estados'),
(40, 'Can add fase partida', 14, 'add_fasepartida'),
(41, 'Can change fase partida', 14, 'change_fasepartida'),
(42, 'Can delete fase partida', 14, 'delete_fasepartida'),
(43, 'Can add grupo', 15, 'add_grupo'),
(44, 'Can change grupo', 15, 'change_grupo'),
(45, 'Can delete grupo', 15, 'delete_grupo'),
(46, 'Can add torneo jugador', 16, 'add_torneojugador'),
(47, 'Can change torneo jugador', 16, 'change_torneojugador'),
(48, 'Can delete torneo jugador', 16, 'delete_torneojugador'),
(49, 'Can add grupo jugador', 17, 'add_grupojugador'),
(50, 'Can change grupo jugador', 17, 'change_grupojugador'),
(51, 'Can delete grupo jugador', 17, 'delete_grupojugador'),
(52, 'Can add num partida', 18, 'add_numpartida'),
(53, 'Can change num partida', 18, 'change_numpartida'),
(54, 'Can delete num partida', 18, 'delete_numpartida'),
(55, 'Can add versus', 19, 'add_versus'),
(56, 'Can change versus', 19, 'change_versus'),
(57, 'Can delete versus', 19, 'delete_versus'),
(58, 'Can add detalle versus', 20, 'add_detalleversus'),
(59, 'Can change detalle versus', 20, 'change_detalleversus'),
(60, 'Can delete detalle versus', 20, 'delete_detalleversus');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', '', '', 'detops.tk@gmail.com', 'pbkdf2_sha256$10000$5zMJptphLnYg$0qZkOT+wuHBT0BZxrp+Fm25CrywcJ0QCfzGRX6fMM10=', 1, 1, 1, '2012-12-10 02:35:27', '2012-12-09 23:13:00'),
(2, 'anibal', 'anibal', 'copitan norabuena', 'acopitan@gmail.com', 'pbkdf2_sha256$10000$7q5vgkI7vAtY$7vNG8wFRfD+v60EnW9JO6v304LNASA1bgzE50WmqdUQ=', 1, 1, 1, '2012-12-10 02:09:41', '2012-12-10 02:05:39');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(3, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `auth_user_user_permissions`
--

INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(3, 2, 31);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Volcar la base de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2012-12-09 23:33:00', 1, 8, '1', 'pepe lucho', 1, ''),
(2, '2012-12-09 23:34:35', 1, 8, '1', 'pepe lucho', 2, 'Changed imagen.'),
(3, '2012-12-09 23:52:42', 1, 12, '1', 'CategoriaJuego object', 1, ''),
(4, '2012-12-09 23:52:48', 1, 12, '1', 'CategoriaJuego object', 2, 'No fields changed.'),
(5, '2012-12-09 23:52:51', 1, 12, '2', 'CategoriaJuego object', 1, ''),
(6, '2012-12-09 23:52:58', 1, 12, '3', 'CategoriaJuego object', 1, ''),
(7, '2012-12-09 23:53:02', 1, 12, '4', 'CategoriaJuego object', 1, ''),
(8, '2012-12-10 02:05:39', 1, 3, '2', 'anibal', 1, ''),
(9, '2012-12-10 02:07:38', 1, 2, '1', 'developer', 1, ''),
(10, '2012-12-10 02:07:57', 1, 2, '2', 'administrator', 1, ''),
(11, '2012-12-10 02:08:06', 1, 3, '2', 'anibal', 2, 'Changed password, first_name, last_name, email, groups and user_permissions.'),
(12, '2012-12-10 02:08:24', 1, 3, '2', 'anibal', 2, 'Changed password.'),
(13, '2012-12-10 02:09:27', 1, 3, '2', 'anibal', 2, 'Changed password, is_staff and is_superuser.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Volcar la base de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'log entry', 'admin', 'logentry'),
(8, 'persona', 'persona', 'persona'),
(9, 'jugador', 'jugador', 'jugador'),
(10, 'pais', 'torneo', 'pais'),
(11, 'torneo', 'torneo', 'torneo'),
(12, 'categoria juego', 'jugador', 'categoriajuego'),
(13, 'estados', 'torneo', 'estados'),
(14, 'fase partida', 'torneo', 'fasepartida'),
(15, 'grupo', 'torneo', 'grupo'),
(16, 'torneo jugador', 'jugador', 'torneojugador'),
(17, 'grupo jugador', 'jugador', 'grupojugador'),
(18, 'num partida', 'versus', 'numpartida'),
(19, 'versus', 'versus', 'versus'),
(20, 'detalle versus', 'versus', 'detalleversus');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7e553563d29bd0c60c1fd5edbca66bf5', 'YjJiYWYzMWRkODA5ODJjYmJhZjk2NzVmM2NjNmI3M2UwNmFmMzM3NTqAAn1xAVUKdGVzdGNvb2tp\nZVUGd29ya2VkcQJzLg==\n', '2012-12-23 23:58:43'),
('d7d7dcd9779a870188945af1ea1b9916', 'NjRmNzVmZDg4ODI1ZDVmNWFmMTRmMjkxYjI3OTI3OGY0MWM3ZTNjMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2012-12-24 02:35:27'),
('7b5e1ae7f6bc74e9ad0c5245c967da3d', 'NWY0MTNmY2ZhYjVjYTEwNGE4NTRlNTcyZDYyNjUyMjE0ZWEzNTYwODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-12-24 02:09:41');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcar la base de datos para la tabla `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugador_categoriajuego`
--

CREATE TABLE IF NOT EXISTS `jugador_categoriajuego` (
  `id_categoria_juego` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  PRIMARY KEY (`id_categoria_juego`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Volcar la base de datos para la tabla `jugador_categoriajuego`
--

INSERT INTO `jugador_categoriajuego` (`id_categoria_juego`, `descripcion`) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C'),
(4, 'D');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugador_grupojugador`
--

CREATE TABLE IF NOT EXISTS `jugador_grupojugador` (
  `id_grupo_jugador` int(11) NOT NULL AUTO_INCREMENT,
  `id_torneo_jugador_id` int(11) NOT NULL,
  `id_grupo_id` int(11) NOT NULL,
  PRIMARY KEY (`id_grupo_jugador`),
  KEY `jugador_grupojugador_649ecd27` (`id_torneo_jugador_id`),
  KEY `jugador_grupojugador_62ee64e3` (`id_grupo_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `jugador_grupojugador`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugador_jugador`
--

CREATE TABLE IF NOT EXISTS `jugador_jugador` (
  `id_jugador` int(11) NOT NULL AUTO_INCREMENT,
  `id_persona_id` int(11) NOT NULL,
  `id_categoria_juego_id` int(11) NOT NULL,
  PRIMARY KEY (`id_jugador`),
  UNIQUE KEY `id_persona_id` (`id_persona_id`),
  KEY `jugador_jugador_77a4708a` (`id_categoria_juego_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcar la base de datos para la tabla `jugador_jugador`
--

INSERT INTO `jugador_jugador` (`id_jugador`, `id_persona_id`, `id_categoria_juego_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugador_torneojugador`
--

CREATE TABLE IF NOT EXISTS `jugador_torneojugador` (
  `id_torneo_jugador` int(11) NOT NULL AUTO_INCREMENT,
  `id_torneo_id` int(11) NOT NULL,
  `id_jugador_id` int(11) NOT NULL,
  `fecha_creacion` date NOT NULL,
  PRIMARY KEY (`id_torneo_jugador`),
  KEY `jugador_torneojugador_2450fea0` (`id_torneo_id`),
  KEY `jugador_torneojugador_1db8672e` (`id_jugador_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `jugador_torneojugador`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona_persona`
--

CREATE TABLE IF NOT EXISTS `persona_persona` (
  `id_persona` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `apellido_parterno` varchar(30) NOT NULL,
  `apellido_materno` varchar(30) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `num_documento` varchar(30) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `direccion_residencia` varchar(100) NOT NULL,
  `direccion_estadia` varchar(100) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `celular` varchar(15) DEFAULT NULL,
  `correo` varchar(75) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `fecha_creacion` date NOT NULL,
  PRIMARY KEY (`id_persona`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcar la base de datos para la tabla `persona_persona`
--

INSERT INTO `persona_persona` (`id_persona`, `nombre`, `apellido_parterno`, `apellido_materno`, `fecha_nacimiento`, `num_documento`, `sexo`, `direccion_residencia`, `direccion_estadia`, `telefono`, `celular`, `correo`, `imagen`, `fecha_creacion`) VALUES
(1, 'pepe lucho', 'villa nueva', 'brusce', '1988-01-01', '45269187', 'M', 'sn', 'sn', '25145145', '12351541', 'detops.tk@gmail.com', 'personas/wallpaper-2222286.jpg', '2012-12-09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneo_estados`
--

CREATE TABLE IF NOT EXISTS `torneo_estados` (
  `id_estado` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `torneo_estados`
--

INSERT INTO `torneo_estados` (`id_estado`, `descripcion`) VALUES
(1, 'lima'),
(2, 'quito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneo_fasepartida`
--

CREATE TABLE IF NOT EXISTS `torneo_fasepartida` (
  `id_fase_partida` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  PRIMARY KEY (`id_fase_partida`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `torneo_fasepartida`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneo_grupo`
--

CREATE TABLE IF NOT EXISTS `torneo_grupo` (
  `id_grupo` int(11) NOT NULL AUTO_INCREMENT,
  `id_torneo_id` int(11) NOT NULL,
  `id_fase_partida_id` int(11) NOT NULL,
  `descripcion` varchar(30) NOT NULL,
  PRIMARY KEY (`id_grupo`),
  KEY `torneo_grupo_2450fea0` (`id_torneo_id`),
  KEY `torneo_grupo_314f2a26` (`id_fase_partida_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `torneo_grupo`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneo_pais`
--

CREATE TABLE IF NOT EXISTS `torneo_pais` (
  `id_pais` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  PRIMARY KEY (`id_pais`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `torneo_pais`
--

INSERT INTO `torneo_pais` (`id_pais`, `descripcion`) VALUES
(1, 'peru'),
(2, 'ecuador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneo_torneo`
--

CREATE TABLE IF NOT EXISTS `torneo_torneo` (
  `id_torneo` int(11) NOT NULL AUTO_INCREMENT,
  `id_pais_id` int(11) NOT NULL,
  `id_estado_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `handicap` varchar(11) NOT NULL,
  `handicap_estado` tinyint(1) NOT NULL,
  `numero_mesas` int(11) NOT NULL,
  `numero_jugadores` int(11) NOT NULL,
  `param_puntos` tinyint(1) NOT NULL,
  `param_promedio` tinyint(1) NOT NULL,
  `param_sm` tinyint(1) NOT NULL,
  `distancia` int(11) NOT NULL,
  `numero_entradas` int(11) NOT NULL,
  `lugar` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `zip_code` varchar(8) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `celular` varchar(15) DEFAULT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_creacion` date NOT NULL,
  PRIMARY KEY (`id_torneo`),
  KEY `torneo_torneo_368be010` (`id_pais_id`),
  KEY `torneo_torneo_2c0a2675` (`id_estado_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `torneo_torneo`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `versus_detalleversus`
--

CREATE TABLE IF NOT EXISTS `versus_detalleversus` (
  `id_detalle_versus` int(11) NOT NULL AUTO_INCREMENT,
  `id_versus_id` int(11) NOT NULL,
  `num_carambola` int(11) NOT NULL,
  PRIMARY KEY (`id_detalle_versus`),
  KEY `versus_detalleversus_7b428e67` (`id_versus_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `versus_detalleversus`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `versus_numpartida`
--

CREATE TABLE IF NOT EXISTS `versus_numpartida` (
  `id_num_partida` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(11) NOT NULL,
  PRIMARY KEY (`id_num_partida`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `versus_numpartida`
--


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `versus_versus`
--

CREATE TABLE IF NOT EXISTS `versus_versus` (
  `id_versus` int(11) NOT NULL AUTO_INCREMENT,
  `id_num_partida_id` int(11) NOT NULL,
  `id_grupo_jugador_id` int(11) NOT NULL,
  PRIMARY KEY (`id_versus`),
  KEY `versus_versus_5a3980c` (`id_num_partida_id`),
  KEY `versus_versus_1b360b3a` (`id_grupo_jugador_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Volcar la base de datos para la tabla `versus_versus`
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
