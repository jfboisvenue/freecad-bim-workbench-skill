# Écarts wiki ↔ code — signatures `make…`

Compare l'ordre des paramètres annoncé par le wiki (couche 1) à celui
réellement défini dans le code (vérité). Un écart d'ordre = risque de
bug silencieux si le LLM passe des arguments positionnels.

**2 divergence(s) détectée(s).**

## ✅ `makeBuilding` — identique
`objectslist, baseobj, name`

## ❌ `makeBuildingPart` — DIVERGENT
- wiki : `objectslist`
- code : `objectslist, baseobj, name`

## ✅ `makeFloor` — identique
`objectslist, baseobj, name`

## ✅ `makeRoof` — identique
`baseobj, facenr, angles, run, idrel, thickness, overhang, name`

## ✅ `makeSectionPlane` — identique
`objectslist, name`

## ✅ `makeSite` — identique
`objectslist, baseobj, name`

## ✅ `makeSpace` — identique
`objects, baseobj, name`

## ✅ `makeStairs` — identique
`baseobj, length, width, height, steps, name`

## ✅ `makeStructure` — identique
`baseobj, length, width, height, name`

## ❌ `makeWall` — DIVERGENT
- wiki : `baseobj, length, width, height, align, face, name`
- code : `baseobj, height, length, width, align, face, name`

## ✅ `makeWindow` — identique
`baseobj, width, height, parts, name`
