1. REFINED CONCEPT — A night sea scene captures the exact, breathless moment of an impossible cosmic catch. A massive, glowing amber full moon—occupying over half the canvas width—is physically snagged by a tiny lone fisherman on a dark wooden skiff far below in a teal-dark sea. The fisherman leans back with desperate, adrenaline-fueled force, his rod strained into a violent arc. A taut, glowing white-gold line runs from the rod tip straight into the moon's lower limb, where a brilliant spark hooks the orb. The sky crackles with kinetic tension: stars streak diagonally downward toward the snagged moon like falling debris, and startled birds flee in terror. The composition drives the eye in a relentless upward-right diagonal, delivering an instant jolt of scale contrast, audacity, and pure momentum.

2. PALETTE —
#0A0E1A  sky top (deep indigo)
#162544  sky bottom (rich twilight)
#04151F  sea deep (dark teal)
#0D3B48  sea surface (vibrant teal)
#FFB703  moon light (warm gold)
#FFE59C  warm highlight (pale amber)
#020408  silhouette ink (near black)
#FF5964  coral accent (fisherman scarf)

3. COMPOSITION — 
- Sky: Rectangle (0, 0, 1024, 768) forming the deep indigo-to-twilight backdrop.
- Sea: Rectangle (0, 768, 1024, 256) for the teal-dark water.
- Waterline/Horizon: Straight line at y = 768.
- Star Field: 12 static small circles scattered in the upper-left quadrant (x: 100-400, y: 50-300, r: 2-4).
- Streaking Star Cluster: 5 angled paths (stroke-width: 2-3) streaking diagonally from top-left (x: 200, y: 150) toward the moon (x: 650, y: 350).
- The Moon: Circle centered at (cx: 650, cy: 380, r: 280), taking up ~55% of the canvas width.
- Moon Halo Ring: Concentric ring around the moon (cx: 650, cy: 380, r: 310, stroke-width: 4).
- Moon Craters: Three overlapping stylized dark amber flat circles inside the moon at (550, 300, 35), (700, 480, 50), (600, 450, 25).
- Broken Light Path: A series of trapezoidal amber bars on the sea surface spanning (x: 500 to 750, y: 768 to 1024).
- The Boat: Small dark polygonal hull at (x: 140, y: 750, w: 60, h: 25).
- The Fisherman: Silhouette shape seated inside boat at (x: 155, y: 730, w: 20, h: 30), leaning hard back to the left.
- The Rod: Curved path (stroke-width: 4) extending from the fisherman's hands (165, 740) curving up and right to (190, 700).
- The Fishing Line: Thin glowing line (stroke-width: 2) running straight from rod tip (190, 700) up to the moon's lower edge at (520, 635).
- The Hook Spark: Diamond polygon centered at (520, 635, size: 16).
- Ripple Rings: Three expanding ellipses centered at the boat (cx: 170, cy: 768), rx/ry scaling outwards: (40, 15), (90, 35), (160, 60), stroke-width: 2.
- The Birds: Three small V-shaped chevron paths fleeing upward-left at positions (300, 400), (330, 380), (280, 430), stroke-width: 3.
Eye travel: Extremely fast, launching instantly from the bottom-left boat along the taut fishing line diagonal up-right toward the moon hook spark in under half a second.

4. DRAW ORDER —
1. Rect element: Sky background, flat fill #0A0E1A.
2. Rect element: Sea background, flat fill #04151F.
3. Path element: Sky-to-sea gradient overlay using linearGradient id "skyGrad" (stops: 0% #0A0E1A, 100% #162544).
4. Group element: Star field dots, flat fill #FFE59C.
5. Group element: Streaking stars, flat stroke #FFE59C, stroke-linecap round.
6. Circle element: Moon halo ring, stroke #FFB703, fill none, stroke-width 4.
7. Circle element: Moon body, flat fill #FFB703.
8. Group element: Moon craters, flat fill #162544 with 30% opacity.
9. Polygon element: Broken light path on sea, linearGradient id "lightPath" (stops: 0% #FFB703, 100% #04151F), opacity 0.8.
10. Group element: Ripple rings around boat, stroke #0D3B48, fill none, stroke-width 2.
11. Path element: Fishing line, stroke #FFE59C, stroke-width 2, fill none.
12. Polygon element: Hook spark at moon edge, flat fill #FFE59C.
13. Path element: Fishing boat hull, flat fill #020408.
14. Path element: Fisherman silhouette, flat fill #020408.
15. Path element: Fisherman scarf, flat fill #FF5964.
16. Path element: Fishing rod, stroke #020408, stroke-width 4, fill none.
17. Group element: Fleeing birds chevrons, stroke #020408, stroke-width 3, fill none, stroke-linecap round.
