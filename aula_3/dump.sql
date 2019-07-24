--
-- PostgreSQL database dump
--

-- Dumped from database version 10.9 (Ubuntu 10.9-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.9 (Ubuntu 10.9-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: rel_usuarios_times; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.rel_usuarios_times (
    id integer NOT NULL,
    usuario integer,
    "time" integer
);


ALTER TABLE public.rel_usuarios_times OWNER TO admin;

--
-- Name: rel_usuarios_times_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.rel_usuarios_times_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rel_usuarios_times_id_seq OWNER TO admin;

--
-- Name: rel_usuarios_times_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.rel_usuarios_times_id_seq OWNED BY public.rel_usuarios_times.id;


--
-- Name: times; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.times (
    id integer NOT NULL,
    nome character varying,
    estadio character varying,
    mundiais integer,
    ano_de_fundacao integer
);


ALTER TABLE public.times OWNER TO admin;

--
-- Name: times_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.times_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.times_id_seq OWNER TO admin;

--
-- Name: times_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.times_id_seq OWNED BY public.times.id;


--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nome character varying,
    email character varying,
    idade integer
);


ALTER TABLE public.usuarios OWNER TO admin;

--
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_id_seq OWNER TO admin;

--
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- Name: rel_usuarios_times id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.rel_usuarios_times ALTER COLUMN id SET DEFAULT nextval('public.rel_usuarios_times_id_seq'::regclass);


--
-- Name: times id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.times ALTER COLUMN id SET DEFAULT nextval('public.times_id_seq'::regclass);


--
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- Data for Name: rel_usuarios_times; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.rel_usuarios_times (id, usuario, "time") FROM stdin;
1	1	1
2	2	1
3	3	4
\.


--
-- Data for Name: times; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.times (id, nome, estadio, mundiais, ano_de_fundacao) FROM stdin;
1	Sport Club Corinthians Paulista	Itaquerão	2	1910
2	Palmeiras	Parque Antartida	0	1914
3	São Paulo	Panetone	3	1950
4	Santos	Vila Belmiro	-1	1960
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.usuarios (id, nome, email, idade) FROM stdin;
1	Lucas Ricciardi de Salles	lucas.salles@4linux.com.br	26
2	Goku Kakaroto	goku@sayajin.com	40
3	Vegeta Príncipe dos Sayajins	vegeta@corporacaocapsula.com	40
\.


--
-- Name: rel_usuarios_times_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.rel_usuarios_times_id_seq', 3, true);


--
-- Name: times_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.times_id_seq', 4, true);


--
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

