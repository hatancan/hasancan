---
baslik: END355 Project Management: Applied Project Management Training Lecture Notes (Prof. Dr. S. Gökhun Tanyer, 2015)
ozet: Notes from Prof. Dr. S. Gökhun Tanyer's Applied Project Management Training (February 21, 2015): course plan, definitions of project and project manager, qualities of a successful project manager, topic outline, sample project exercise, and file naming conventions.
---

This post is a summary of the **"Applied Project Management Training"** (*Project Management and Its Applications*) documents prepared by **Prof. Dr. S. Gökhun Tanyer** (Başkent University, Electrical-Electronics Engineering) in the END355 Project Management folder. The training was planned as a 10-hour course on February 21, 2015 (5 hours of lectures, 2 hours of in-class practice, 3 hours of practice assignment); certificates are jointly issued by BEDAM, the Faculty of Engineering, and SMART A.Ş. The slides are based mainly on the **PMBOK Guide** (2008) and **ISO/IEC 12207 – IEEE 12207** (software life cycle). The six original PDFs can be downloaded in the ZIP at the end of the post; figures taken from the source books are not included in this post.

## 1A – Introduction

**Time schedule:** 09:30–10:20 Introduction; 10:30–11:20 PM definitions; 11:30–13:00 PM areas of expertise; 14:30–15:20 process management; 15:30–16:00 sample project exercise; 16:10–17:00 free PM exercise; 17:10–18:00 project submission; followed by approximately 2 hours of homework.

**Questions to be answered:** What is a project? Who is a project manager and who is a project executor? What is project management? Who makes up the project team? What does stakeholder mean? What is needed for a successful project? What are processes and process management in project management?

**Successful project:** delivering the product the customer wants in full, on-time delivery, completion within budget, and "survival of the project team". Target audience: students, researchers, project managers, customers, personnel, and stakeholders. Possible fields of impact include MSB (Ministry of National Defence), SSM (Presidency of Defence Industries), Horizon 2020, TÜBİTAK (1001, 1501, TEYDEP), BAP (Scientific Research Projects), and in-house projects. As background, basic algebra, the ability to question a problem, and knowledge of MS Excel/Word/Project are recommended.

The problems experienced in standard courses are listed as follows: remaining purely theoretical, not matching personal needs, the instructor's limited project management experience, course materials not being handed out, and lack of retention because the knowledge is not applied. In this course, a week's worth of course material is summarized in one day; basic background is covered before noon and practice in the afternoon; the language is Turkish, and English equivalents of the terms are also given. It is noted that at least one project process and about one year are required for the content to truly sink in.

**Course scope:** 1) Introduction and basic definitions; 2) Project management–1 (life cycle, definition of success, managed processes, strategies, uncertainties, and common mistakes); 3) Project management–2 (scheduling, organization building, different approaches); 4) Processes (initiation, requirements determination, design, implementation, testing, closure).

## 1B – Topic outline and general definitions

Topic outline: introduction; definitions (project, project management, project manager, history, project management offices); areas of expertise (scope, time, cost, quality, human resources, communication, risk, contract/procurement/stakeholder management; uncertainties and common mistakes); process management (IEEE 12207 software life cycle: architecture, phases, products, evaluations, audits, reviews, baselines, configuration management).

**What is a project?** By Gary R. Heerkens' (PMI) definition: a set of activities, defined by a temporary duration, that includes any kind of work aimed at obtaining a product or service. The requirements for being a project are: {duration, product/service, work}. Organizational hierarchy: strategy → portfolio → program → project → subproject.

**The project manager** is the person responsible for the success or failure of a project. The project executor is a person who applies exactly the procedures and methods imposed on them, and who is bound by regulation on matters such as dismissing personnel, budget revisions, and time extensions; the manager, on the other hand, manages the project with the authority and responsibility given to them. The manager sees "the glass half full" and focuses on what has been achieved, whereas the team generally focuses on what the manager has failed to achieve; both sides need to behave correctly for the project to succeed.

- **Positive aspects:** chance of advancement in the work environment, a strong sense of "I did it", variety, freedom, the chance to influence the organization.
- **Negative aspects:** politics in the work environment; uncertainty; lack of authority commensurate with responsibility; drifting away from the technical world; the perception of "not doing real work"; the pressure of "two bosses".
- **Unofficial duties:** babysitter, salesperson, teacher, friend.
- **Required qualities (PMBOK 2007):** solution-oriented, loves their work, outgoing, a role model (leader), a good manager, analytical thinker.
- **Areas of responsibility (PMBOK 2004):** the customer, the organization, the project, the project team, and themselves.
- **Four messages for a successful manager:** (1) "You and the work you do are important", (2) "I trust you and your ability", (3) notice work that is done well, (4) set an example.
- Regarding problems among employees: problems caused by overconfidence, low self-confidence, and weak management; the solutions are clear duties/responsibilities, realistic schedule pressure, and teams of equivalent self-confidence. Also: reward the "messenger" who reports problems, reward early reporting of problems, and do not badmouth one member to another. "Project management = science + art." Proceed step by step: plan, take a step, check, repeat.
- **Final word:** for success, the project manager must have responsibility **and authority** and must be able to **use** that authority.

**Project management** (Heerkens): the application of knowledge, experience, skills, tools/equipment, and other techniques to meet project needs.

## 2A – Applied sample project exercise

The practical part of the course aims to prepare realistic project documents in groups of one to at most three people. Sample project: the development of a **"Programmable Musical Instrument"** for children aged 4–12 in military kindergartens, through a tender by the Ministry of National Defence Directorate of Domestic Procurement (it is assumed that Başkent University won the tender). The exercise produces the following documents in order: contract, project statement of work document (PİTD), project definition (technical specifications) document (PTD), official correspondence, project initiation (kick-off meeting), concept definition and operations document (KTİD), and work breakdown structure document (İKAD; hardware and software work packages, a study of Arduino vs. MCU, etc.). The instrument will make the tuning systems programmable for Western music (piano, equal temperament) and Turkish music (KTSM and THM), be suitable for children, and be able to run on mains power and a rechargeable battery.

The 2B file in the ZIP is a blank worksheet that participants can fill in with their own project title.

## File naming conventions (Tanyer, November 27, 2014)

The recommended naming format for performing version control without using any software:

`<ANABASLIK-ALTBASLIK-DetayliBilgiKodu-SXDZZ-YYAAGG-ISIMS.zzz>`

- **Main heading:** the most general uppercase code indicating the scope of the file (e.g., `MUH` Faculty of Engineering, `EEM224` course document, `TUBITAK1001`, `PRJ` project).
- **Subheading:** second-level code (e.g., `MUH-RY` official letter, `EEM224-AS` midterm exam, `TUBITAK1001-PBF` project application form).
- **Detailed information code:** optional; words are joined without spaces, with each word capitalized.
- **SXDZZ:** version and revision; **YYAAGG:** year-month-day; **ISIMS:** abbreviation of the preparer.

Thanks to this method, the date, preparer, scope, and version of a document can be understood from the file name; files from different people remain in the same directory without getting mixed up under automatic sorting.
