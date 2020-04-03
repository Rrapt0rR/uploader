--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4 (Debian 10.4-2.pgdg90+1)
-- Dumped by pg_dump version 10.4 (Debian 10.4-2.pgdg90+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
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
-- Name: user; Type: TABLE; Schema: public; Owner: mastermanager
--

CREATE TABLE public.user (
    id integer NOT NULL,
    email character varying(120),
    password_hash character varying(128),
    user_name character varying(120),
    reset_code character varying(10),
    phone character varying(120),
    verified character varying(10),
    verification_code character varying(10),
    is_admin character varying(10),
    is_banned character varying(5)
);


ALTER TABLE public.user OWNER TO mastermanager;

--
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: mastermanager
--

CREATE SEQUENCE public.user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_id_seq OWNER TO mastermanager;

--
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mastermanager
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public.user.id;


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: mastermanager
--

ALTER TABLE ONLY public.user ALTER COLUMN id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: mastermanager
--

COPY public.user (id, email, password_hash, user_name, user_account_name, reset_code, title, phone, ext, mobile, verified, verification_code, is_admin, is_banned) FROM stdin;
1	peanut@pbf.org	pbkdf2:sha256:50000$hLxscNG5$15fec6e0fda7e431fce85eb286322715c1a0cb4a096d9e363f3b32759194c01d	dev user	Master	\N	\N	+11234567890	\N	\N	yes	V2SFS2VD43	yes	no
\.


--
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mastermanager
--

SELECT pg_catalog.setval('public.user_user_id_seq', 1, false);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: mastermanager
--

ALTER TABLE ONLY public.user
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: mastermanager
--

CREATE UNIQUE INDEX ix_user_email ON public.user USING btree (email);


--
-- PostgreSQL database dump complete
--

