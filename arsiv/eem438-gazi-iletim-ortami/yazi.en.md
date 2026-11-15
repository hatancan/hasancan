---
baslik: EEM438 Data Communications: Transmission Media: Twisted Pair, Coaxial, Fiber, and Wireless (Gazi University, Suat Özdemir)
ozet: Data Communications lecture slides by Suat Özdemir of Gazi University: guided (twisted pair, coaxial, fiber optic) and unguided transmission media, SDH/SONET.
---

These are the Chapter 7 (Transmission Media) slides that Suat Özdemir of the Department of Computer Engineering at Gazi University prepared for the course "Veri İletişimi / Data Communications" (slide date 21 March 2011; the footer reads BM 403 Data Communications). They are kept in the EEM438 folder as course material from a second instructor. The slide text is transcribed below; figures and tables taken from the textbook are not published, and slides without text are noted. The original PDF can be downloaded at the end of the post.

Scope: guided (twisted pair, coaxial, fiber optic) and unguided transmission media, SDH/SONET.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## Introduction

- Transmission media is anything that carries information between a source and a destination.
- Transmission media lie below the physical layer and are controlled by the physical layer.
- Transmission media can be metallic cable, fiber optic, or free space.
- Communication over long distances using electrical signals began in the 1900s with Morse's invention of the telegraph.
- The first telephone was invented in 1869.

## Introduction (2)

- Wireless communication was first carried out by Hertz in 1895 using high-frequency signals.
- Better metallic cables (twisted pair, coaxial cable) were developed.
- The use of fiber optics has increased communication speeds dramatically.
- With modulation and multiplexing techniques, free space has been used effectively for data communication.
- The electromagnetic spectrum consists of radio waves, infrared, visible light, ultraviolet light, X-rays, gamma rays, and so on.

## Guided Media

- Twisted-pair cable, coaxial cable, and fiber optic cable are called guided media.
- Twisted-pair cable

## Twisted-pair cable

- One of the wires is used to carry the signal and the other is used as a ground reference.
- In a twisted cable, noise affects both wires equally. The receiver evaluates the difference between the two wires.

## Twisted-pair cable (2)

- Communication generally uses unshielded twisted-pair (UTP). IBM produced shielded twisted-pair (STP) cable.
- The RJ45 (registered jack 45) connector is used for UTP cables.

## Twisted-pair cable (3)

- UTP cables have been classified by the EIA (Electronic Industries Association).

## Twisted-pair cable (4)

- The performance of twisted-pair cable is measured by attenuation as a function of frequency and distance. In the figure, the gauge indicates the AWG number and relates to the thickness of the wire.

## Twisted-pair cable (5)

- UTP cables are used for voice and data communication on telephone lines.
- UTP cables are used for high-speed communication on DSL lines.
- Twisted-pair cables are used in local area networks such as 10Base-T and 100Base-T.

## Coaxial cable

- Coaxial cable carries signals in a higher frequency range than twisted-pair cable.
- Coaxial cable has a conductor at its center.

## Coaxial cable (2)

- Coaxial cable is classified by RG (radio government) ratings.
- The BNC (Bayonet Neill-Concelman) connector is used as the connector.

## Coaxial cable (3)

- The performance of coaxial cable can be measured in the same way as for twisted-pair cable.
- The figure shows the variation with the ratio of the inner conductor and shield diameters.

## Coaxial cable (4)

- Coaxial cable is used in analog telephone networks (one coax cable carries 10,000 voice signals).
- It is used in digital telephone networks (one coax cable carries 600 Mbps of digital data).
- Coax cable (RG-59) is used in cable TV networks.
- It is used in Ethernet networks (10Base-2 and thin Ethernet use RG-58 (10 Mbps, 185 m); 10Base-5 and thick Ethernet use RG-11 (10 Mbps, 5,000 m)).

## Fiber optic cable

- Fiber optic cable is made of glass or plastic and transmits light signals.
- Light changes direction when it passes through media of different densities.
- Fiber optics controls light through the property of reflection.

## Fiber optic cable (2)

- Fiber optic cable can support multimode or single mode propagation.
- Multimode comes in two types: step-index and graded-index.

## Fiber optic cable (3)

- In multimode propagation, many light beams leave the source along different paths.
- In multimode step-index fiber, the density of the core is constant from the center to the edges.
- In multimode graded-index fiber, the density of the core decreases from the center toward the edges.
- In single mode fiber, the core diameter is very small and the source light is very tightly focused.

## Fiber optic cable (4)

*This slide contains only figures/tables; the image is in the original PDF.*


## Fiber optic cable (5)

- The size of fiber optic cables is determined by the diameter of the core and the diameter of the cladding.

## Fiber optic cable (6)

- The outer jacket is made of PVC or Teflon. Kevlar makes the cable durable.
- Three types of connectors are used. The SC (subscriber connector) is used for cable TV.
- The ST (straight tip) is used for connecting to network devices.
- The MT-RJ (Mechanical Transfer Registered Jack) is the same size as the RJ45.

## Fiber optic cable (7)

- The performance is as shown in the figure.

## Fiber optic cable (8)

- Because of its wide bandwidth, it is used in backbone networks.
- With WDM, communication at 1600 Gbps (1.6 Tbps) is possible.
- It is used in SONET (Synchronous Optical NETwork) networks.
- Fiber optic cable is used in local area networks (100Base-FX and 1000Base-X).

## SDH/SONET

- The goal of fiber optic communication is to carry the most data over the longest distance with the least loss.
- The most critical aspect of network robustness is that link problems or failures in network elements are detected within a few tens of milliseconds and the necessary measures are taken, without interrupting the services provided to users.

## SDH/SONET (2)

- SDH/SONET technologies offer a high degree of reliability and availability. Service providers need an availability of between 99.99% and 99.999% for the services provided over the network.
- These figures correspond to an average of 3 to 5 minutes of downtime per year in the network.
- SDH/SONET networks achieve this performance through sophisticated service-protection mechanisms.

## SDH/SONET (3)

- By multiplexing several data-modulated wavelengths onto the same fiber with WDM, it has become possible to carry many optical channels, each with equal data capacity, on a single fiber.

## SDH/SONET (4)

- SDH/SONET technology has continued to evolve over decades in line with growing traffic diversity and needs.
- Service providers have needed to carry Gigabit Ethernet (GE) traffic together with the time-division multiplexed traffic carried over the well-established and proven SDH/SONET.
- To carry ATM, Ethernet, and TDM traffic together, SDH/SONET technology has turned toward Next Generation Networks (NGN), which can provide multiservice offerings.

## Fiber optic cable (9)

- Advantages
  - High bandwidth
  - Low signal attenuation
  - Immune to electromagnetic noise
  - More resistant to corrosion
  - Light weight
  - Secure. At connection points, it does not create an antenna effect as copper cables do.
- Disadvantages
  - Installation and operation require skilled personnel.
  - Light is unidirectional; two fiber optic cables are needed for two-way communication.
  - High cost.

## Unguided media

- Wireless media carry electromagnetic waves without a physical conductor.
- This type of communication is called wireless communication (wireless networks).
- The electromagnetic spectrum used in wireless communication spans 3 kHz-900 THz.

## Unguided media (2)

- Unguided signals propagate from source to destination in three ways: ground propagation, sky propagation, and line-of-sight (LOS).

## Ground Wave Propagation

- Follows the Earth's surface
  - Electromagnetic waves induce currents in the Earth's surface, which slow and bend the signal
  - Diffraction
- Can travel very long distances
- Used for frequencies up to 2 MHz
- Example
  - AM radio

## Sky Wave Propagation

- The signal is reflected between the ionosphere layer of the atmosphere and the Earth's surface
- The signal can bounce back and forth between the ionosphere and the Earth's surface many times
- The reflection effect is caused by refraction
- Examples
  - Amateur radio (wireless communication)
  - BBC International, Voice of America

## Line-of-Sight Propagation
- The transmitting and receiving antennas must be within each other's line of sight
  - Satellite communication – signals above 30 MHz are not reflected by the ionosphere
  - Ground communication – the antennas are within each other's effective line of sight

## Effective (Radio) Line of Sight

*This slide contains only figures/tables; the image is in the original PDF.*


## Line-of-Sight Equations

- Optical line of sight: d = 3.57 √h
- Effective, or radio, line of sight: d = 3.57 √(K·h)
- d = distance between the antenna and the horizon (km)
- h = antenna height (m)
- K = refraction factor; as a rule of thumb, K = 4/3

## Line-of-Sight Equations (2)

- Maximum distance between two antennas for line of sight (LOS): d = 3.57 (√(K·h1) + √(K·h2))
- h1 = height of the 1st antenna
- h2 = height of the 2nd antenna

## Unguided media (3)

- Microwaves and radio waves in the electromagnetic spectrum are shown in 8 bands.

## Unguided media (4)

- Wireless communication is divided into three groups: radio waves, microwaves, and infrared waves.

## Unguided media (5)

- Radio waves
  - Electromagnetic waves with frequencies between 3 kHz and 1 GHz are called radio waves, and those between 1 GHz and 300 GHz are called microwaves.
  - Radio waves propagate omnidirectionally (in all directions).
  - The transmitting and receiving antennas do not need to be aligned.
  - Radio waves propagate in sky mode and can travel long distances.
  - AM radios use radio waves.

## Unguided media (6)

- Microwaves
  - They occupy the band between 1 GHz and 300 GHz.
  - Microwaves propagate unidirectionally.
  - The transmitting and receiving antennas must be aligned. Microwaves propagate by LOS.
  - Repeaters are required over long distances.
  - Microwaves at very high frequencies cannot pass through walls.
  - Parabolic dish antennas or horn antennas are used.

## Unguided media (7)

- Infrared waves
  - They occupy the band between 300 GHz and 400 THz (wavelengths of 1 mm-770 nm).
  - Used for short-distance communication.
  - Cannot pass through walls.
  - Used in enclosed environments.
  - The IrDA (Infrared Data Association) port on a computer is used to connect a keyboard, mouse, or printer.
  - Communication is by LOS.

*Note: The square-root signs in the line-of-sight formulas were lost in the PDF text; they have been restored in the form d = 3.57·√(K·h).*
