import random

APPLICATION = "amzn1.ask.skill.1c223c43-5393-44c0-8587-35f843e7175f"

VOCAB = {
    "a": [
    { "category": "interjection",
     "definition": "ah, ha, uh, oh, ooh, aw, well (emotion word)"
    }
  ],

  "akesi": [
    { "category": "noun",
      "definition": "creeping animal, a scaly or slimy animal that creeps on land"
    },
    { "category": "noun",
      "definition": "reptile, any air-breathing cold-blooded animal that crawls on land and has scales and bones; reptile"
    },
    { "category": "noun",
      "definition": "amphibian, any cold-blooded animal with bones that lives on both land and in water; amphibian"
    },
    { "category": "noun",
      "definition": "large arthropod, a large arthropod that lives on land; scorpion"
    },
    { "category": "describer",
      "definition": "like an akesi in appearance"
    },
    { "category": "describer",
      "definition": "the characteristics or properties of an akesi"
    }
  ],

  "ala" : [
    {
      "category": "modifier",
      "definition": "no, not, none, un-"
    },
    {
      "category": "noun",
      "definition": "nothing, negation, zero"
    },
    {
      "category": "interjection",
      "definition": "no!"
    },
    {
      "category": "describer",
      "definition": "not, not such; no, not"
    },
    {
      "category": "describer",
      "definition": "no, zero, no quantity of; no, zero"
    },
    {
      "category": "describer",
      "definition": "un-, opposite of; un-"
    },
    {
      "category": "noun",
      "definition": "the state, situation or general phenomenon of being ala; absence, emptiness, negation, nothing, zero"
    },
    {
      "category": "interjection",
      "definition": "a short, sudden or emotional expression of ala; no!"
    }
  ],

  "alasa" : [
    {
      "category": "transitive verb",
      "definition": "to gather, to collect food, resources or material needed for daily life and survival; to gather, harvest"
    },
    {
      "category": "transitive verb",
      "definition": "to hunt, to pursue and kill animals to use as food and clothing; to hunt"
    }
  ],

  "ale" : [
    {
      "category": "noun",
      "definition": "everything, anything, life, the universe"
    },
    {
      "category": "modifier",
      "definition": "all, every, complete, whole"
    }
  ],

  "anpa" : [
    {
      "category": "noun",
      "definition": "bottom, lower part, under, below, floor, beneath"
    },
    {
      "category": "modifier",
      "definition": "low, lower, bottom, down"
    }
  ],

  "ante" : [
    {
      "category": "noun",
      "definition": "difference"
    },
    {
      "category": "modifier",
      "definition": "different"
    },
    {
      "category": "conjunction",
      "definition": "otherwise, or else"
    },
    {
      "category": "transitive verb",
      "definition": "change, alter, modify"
    }
  ],

  "anu" : [
    {
      "category": "conjunction",
      "definition": "or"
    }
  ],

  "awen" : [
    {
      "category": "intransitive verb",
      "definition": "stay, wait, remain"
    },
    {
      "category": "transitive verb",
      "definition": "to keep"
    },
    {
      "category": "modifier",
      "definition": "remaining, stationary, permanent, sedentary"
    }
  ],

  "e" : [
    {
      "alphaBreak": "true",
      "category": "separator",
      "definition": "(introduces a direct object)"
    }
  ],

  "en" : [
    {
      "category": "conjunction",
      "definition": "and (used to coordinate head nouns)"
    }
  ],

  "esun" : [
    {
      "category": "noun",
      "definition": "market, shop"
    }
  ],

  "ijo" : [
    {
      "alphaBreak": "true",
      "category": "noun",
      "definition": "thing, something, stuff, anything, object"
    },
    {
      "category": "modifier",
      "definition": "of something"
    },
    {
      "category": "transitive verb",
      "definition": "objectify"
    }
  ],

  "ike" : [
    {
      "category": "modifier",
      "definition": "bad, negative, wrong, evil, overly complex, (figuratively) unhealthy"
    },
    {
      "category": "interjection",
      "definition": "oh dear! woe! alas!"
    },
    {
      "category": "noun",
      "definition": "negativity, badness, evil"
    },
    {
      "category": "transitive verb",
      "definition": "to make bad, to worsen, to have a negative effect upon"
    },
    {
      "category": "intransitive verb",
      "definition": "to be bad, to suck"
    }
  ],

  "ilo" : [
    {
      "category": "noun",
      "definition": "tool, device, machine, thing used for a specific purpose"
    }
  ],

  "insa" : [
    {
      "category": "noun",
      "definition": "inside, inner world, centre, stomach"
    },
    {
      "category": "modifier",
      "definition": "inner, internal"
    }
  ],

  "jaki" : [
    {
      "alphaBreak": "true",
      "category": "modifier",
      "definition": "dirty, gross, filthy"
    },
    {
      "category": "noun",
      "definition": "dirt, pollution, garbage, filth"
    },
    {
      "category": "transitive verb",
      "definition": "pollute, dirty"
    },
    {
      "category": "interjection",
      "definition": "ew! yuck!"
    }
  ],

  "jan" : [
    {
      "category": "noun",
      "definition": "person, people, human, being, somebody, anybody"
    },
    {
      "category": "modifier",
      "definition": "human, somebody's, personal, of people"
    },
    {
      "category": "transitive verb",
      "definition": "personify, humanize, personalize"
    }
  ],

  "jelo" : [
    {
      "category": "modifier",
      "definition": "yellow, light green"
    }
  ],

  "jo" : [
    {
      "category": "transitive verb",
      "definition": "have, contain"
    },
    {
      "category": "noun",
      "definition": "having"
    },
    {
      "category": "kama",
      "definition": "receive, get, take, obtain"
    }
  ],

  "kala" : [
    {
      "alphaBreak": "true",
      "category": "noun",
      "definition": "fish, sea creature"
    }
  ],

  "kalama" : [
    {
      "category": "noun",
      "definition": "sound, noise, voice"
    },
    {
      "category": "intransitive verb",
      "definition": "make noise"
    },
    {
      "category": "transitive verb",
      "definition": "sound, ring, play (an instrument)"
    }
  ],

  "kama" : [
    {
      "category": "intransitive verb",
      "definition": "come, become, arrive, happen, pursue actions to arrive to (a certain state), manage to, start to"
    },
    {
      "category": "noun",
      "definition": "event, happening, chance, arrival, beginning"
    },
    {
      "category": "modifier",
      "definition": "coming, future"
    },
    {
      "category": "transitive verb",
      "definition": "bring about, summon"
    }
  ],

  "kasi" : [
    {
      "category": "noun",
      "definition": "plant, leaf, herb, tree, wood"
    }
  ],

  "ken" : [
    {
      "category": "intransitive verb",
      "definition": "can, is able to, is allowed to, may, is possible"
    },
    {
      "category": "noun",
      "definition": "possibility, ability, power to do things, permission"
    },
    {
      "category": "transitive verb",
      "definition": "to make possible, enable, allow, permit"
    },
    {
      "category": "cont",
      "definition": "it is possible that"
    }
  ],

  "kepeken" : [
    {
      "category": "transitive verb",
      "definition": "to use"
    },
    {
      "category": "prep",
      "definition": "with"
    }
  ],

  "kili" : [
    {
      "category": "noun",
      "definition": "fruit, pulpy vegetable, mushroom"
    }
  ],

  "kin" : [
    {
      "category": "modifier",
      "definition": "also, too, even, indeed (emphasizes the word(s) before it)"
    }
  ],

  "kipisi" : [
    {
      "category": "transitive verb",
      "definition": "to cut"
    }
  ],

  "kiwen" : [
    {
      "category": "modifier",
      "definition": "hard, solid, stone-like, made of stone or metal"
    },
    {
      "category": "noun",
      "definition": "hard thing, rock, stone, metal, mineral, clay"
    }
  ],

  "ko" : [
    {
      "category": "noun",
      "definition": "semi-solid or squishy substance, e.g. paste, powder, gum"
    }
  ],

  "kon" : [
    {
      "category": "noun",
      "definition": "air, wind, smell, soul"
    },
    {
      "category": "modifier",
      "definition": "air-like, ethereal, gaseous"
    }
  ],

  "kule" : [
    {
      "category": "noun",
      "definition": "colour, paint"
    },
    {
      "category": "modifier",
      "definition": "colourful"
    },
    {
      "category": "transitive verb",
      "definition": "colour, paint"
    }
  ],

  "kute" : [
    {
      "category": "transitive verb",
      "definition": "to listen, to hear"
    },
    {
      "category": "modifier",
      "definition": "auditory, hearing"
    }
  ],

  "kulupu" : [
    {
      "category": "noun",
      "definition": "group, community, society, company, people"
    },
    {
      "category": "modifier",
      "definition": "communal, shared, public, of the society"
    }
  ],

  "la" : [
    {
      "alphaBreak": "true",
      "category": "separator",
      "definition": "(between adverb or phrase of context and sentence)"
    }
  ],

  "lape" : [
    {
      "category": "noun",
      "definition": "sleep, rest"
    },
    {
      "category": "intransitive verb",
      "definition": "to sleep, to rest"
    },
    {
      "category": "modifier",
      "definition": "sleeping, of sleep"
    }
  ],

  "laso" : [
    {
      "category": "modifier",
      "definition": "blue, blue-green"
    }
  ],

  "lawa" : [
    {
      "category": "noun",
      "definition": "head, mind"
    },
    {
      "category": "modifier",
      "definition": "main, leading, in charge"
    },
    {
      "category": "transitive verb",
      "definition": "lead, control, rule, steer"
    }
  ],

  "len" : [
    {
      "category": "noun",
      "definition": "clothing, cloth, fabric"
    }
  ],

  "lete" : [
    {
      "category": "noun",
      "definition": "cold"
    },
    {
      "category": "modifier",
      "definition": "cold, uncooked"
    },
    {
      "category": "transitive verb",
      "definition": "cool down, chill"
    }
  ],

  "li" : [
    {
      "category": "separator",
      "definition": "(between any subject except mi and sina and its verb; also used to introduce a new verb for the same subject)"
    }
  ],

  "lili" : [
    {
      "category": "modifier",
      "definition": "small, little, young, a bit, short, few, less"
    },
    {
      "category": "transitive verb",
      "definition": "reduce, shorten, shrink, lessen"
    }
  ],

  "linja" : [
    {
      "category": "noun",
      "definition": "long, very thin, floppy thing, e.g. string, rope, hair, thread, cord, chain"
    }
  ],

  "lipu" : [
    {
      "category": "noun",
      "definition": "flat and bendable thing, e.g. paper, card, ticket"
    }
  ],

  "loje" : [
    {
      "category": "modifier",
      "definition": "red"
    }
  ],

  "lon" : [
    {
      "category": "quasi-preposition",
      "definition": "be (located) in/at/on"
    },
    {
      "category": "intransitive verb",
      "definition": "to be there, be present, be real/true, exist, be awake"
    }
  ],

  "luka" : [
    {
      "category": "noun",
      "definition": "hand, arm"
    }
  ],

  "lukin" : [
    {
      "category": "transitive verb",
      "definition": "see, look at, watch, read"
    },
    {
      "category": "intransitive verb",
      "definition": "look, watch out, pay attention"
    },
    {
      "category": "modifier",
      "definition": "visual(ly)"
    }
  ],

  "lupa" : [
    {
      "category": "noun",
      "definition": "hole, orifice, window, door"
    }
  ],

  "ma" : [
    {
      "alphaBreak": "true",
      "category": "noun",
      "definition": "land, earth, country, (outdoor) area"
    }
  ],

  "mama" : [
    {
      "category": "noun",
      "definition": "parent, mother, father"
    },
    {
      "category": "modifier",
      "definition": "of the parent, parental, maternal, fatherly"
    }
  ],

  "mani" : [
    {
      "category": "noun",
      "definition": "money, material wealth, currency, dollar, capital"
    }
  ],

  "meli" : [
    {
      "category": "noun",
      "definition": "woman, female, girl, wife, girlfriend"
    },
    {
      "category": "modifier",
      "definition": "female, feminine, womanly"
    }
  ],

  "mi" : [
    {
      "category": "noun",
      "definition": "I, we"
    },
    {
      "category": "modifier",
      "definition": "my, our"
    }
  ],

  "mije" : [
    {
      "category": "noun",
      "definition": "man, male, boy, husband, boyfriend"
    },
    {
      "category": "transitive verb",
      "definition": "male, masculine, manly"
    }
  ],

  "moku" : [
    {
      "category": "noun",
      "definition": "food, meal"
    },
    {
      "category": "transitive verb",
      "definition": "eat, drink, swallow, ingest, consume"
    }
  ],

  "moli" : [
    {
      "category": "noun",
      "definition": "death"
    },
    {
      "category": "intransitive verb",
      "definition": "die, be dead"
    },
    {
      "category": "transitive verb",
      "definition": "kill"
    },
    {
      "category": "modifier",
      "definition": "dead, deadly, fatal"
    }
  ],

  "monsi" : [
    {
      "category": "noun",
      "definition": "back, rear end, butt, behind"
    },
    {
      "category": "modifier",
      "definition": "back, rear"
    }
  ],

  "mu" : [
    {
      "category": "interjection",
      "definition": "woof! meow! moo! etc. (cute animal noise)"
    }
  ],

  "mun" : [
    {
      "category": "noun",
      "definition": "moon"
    },
    {
      "category": "modifier",
      "definition": "lunar"
    }
  ],

  "musi" : [
    {
      "category": "noun",
      "definition": "fun, playing, game, recreation, art, entertainment"
    },
    {
      "category": "modifier",
      "definition": "artful, fun, recreational"
    },
    {
      "category": "intransitive verb",
      "definition": "play, have fun"
    },
    {
      "category": "transitive verb",
      "definition": "amuse, entertain"
    }
  ],

  "mute" : [
    {
      "category": "modifier",
      "definition": "many, very, much, several, a lot, abundant, numerous, more"
    },
    {
      "category": "noun",
      "definition": "amount, quantity"
    },
    {
      "category": "transitive verb",
      "definition": "make many or much"
    }
  ],

  "namako" : [
    {
      "alphaBreak": "true",
      "category": "noun",
      "definition": "spice"
    },
    {
      "category": "modifier",
      "definition": "extra, additional"
    }
  ],

  "nanpa" : [
    {
      "category": "noun",
      "definition": "number"
    },
    {
      "category": "oth",
      "definition": "-th (ordinal numbers)"
    }
  ],

  "nasa" : [
    {
      "category": "modifier",
      "definition": "silly, crazy, foolish, drunk, strange, stupid, weird"
    },
    {
      "category": "transitive verb",
      "definition": "crazy, make weird"
    }
  ],

  "nasin" : [
    {
      "category": "noun",
      "definition": "way, manner, custom, road, path, doctrine, system, method"
    }
  ],

  "nena" : [
    {
      "category": "noun",
      "definition": "bump, nose, hill, mountain, button"
    }
  ],

  "ni" : [
    {
      "category": "modifier",
      "definition": "this, that"
    }
  ],

  "nimi" : [
    {
      "category": "noun",
      "definition": "word, name"
    }
  ],

  "noka" : [
    {
      "category": "noun",
      "definition": "leg, foot"
    }
  ],

  "o" : [
    {
      "alphaBreak": "true",
      "category": "separator",
      "definition": "O (vocative or imperative)"
    },
    {
      "category": "interjection",
      "definition": "hey! (calling somebody's attention)"
    }
  ],

  "oko" : [
    {
      "category": "noun",
      "definition": "eye"
    }
  ],

  "olin" : [
    {
      "category": "noun",
      "definition": "love"
    },
    {
      "category": "modifier",
      "definition": "love"
    },
    {
      "category": "transitive verb",
      "definition": "to love (a person)"
    }
  ],

  "ona" : [
    {
      "category": "noun",
      "definition": "she, he, it, they"
    },
    {
      "category": "modifier",
      "definition": "her, his, its, their"
    }
  ],

  "open" : [
    {
      "category": "transitive verb",
      "definition": "to open, turn on"
    }
  ],

  "pakala" : [
    {
      "alphaBreak": "true",
      "category": "noun",
      "definition": "blunder, accident, mistake, destruction, damage, breaking"
    },
    {
      "category": "transitive verb",
      "definition": "screw up, fuck up, botch, ruin, break, hurt, injure, damage, spoil, ruin"
    },
    {
      "category": "intransitive verb",
      "definition": "screw up, fall apart, break"
    },
    {
      "category": "interjection",
      "definition": "damn! fuck!"
    }
  ],

  "pali" : [
    {
      "category": "noun",
      "definition": "activity, work, deed, project"
    },
    {
      "category": "modifier",
      "definition": "active, work-related, operating, working"
    },
    {
      "category": "transitive verb",
      "definition": "do, make, build, create"
    },
    {
      "category": "intransitive verb",
      "definition": "act, work, function"
    }
  ],

  "palisa" : [
    {
      "category": "noun",
      "definition": "long, mostly hard object, e.g. rod, stick, branch"
    }
  ],

  "pan" : [
    {
      "category": "noun",
      "definition": "grain, cereal"
    }
  ],

  "pana" : [
    {
      "category": "transitive verb",
      "definition": "give, put, send, place, release, emit, cause"
    },
    {
      "category": "noun",
      "definition": "giving, transfer, exchange"
    }
  ],

  "pata" : [
    {
      "category": "noun",
      "definition": "brother"
    }
  ],

  "pi" : [
    {
      "category": "separator",
      "definition": "of, belonging to"
    }
  ],

  "pilin" : [
    {
      "category": "noun",
      "definition": "feelings, emotion, heart"
    },
    {
      "category": "intransitive verb",
      "definition": "feel"
    },
    {
      "category": "transitive verb",
      "definition": "to feel, think, sense, touch"
    }
  ],

  "pimeja" : [
    {
      "category": "modifier",
      "definition": "black, dark"
    },
    {
      "category": "noun",
      "definition": "darkness, shadows"
    },
    {
      "category": "transitive verb",
      "definition": "darken"
    }
  ],

  "pini" : [
    {
      "category": "noun",
      "definition": "end, tip"
    },
    {
      "category": "modifier",
      "definition": "completed, finished, past, done, ago"
    },
    {
      "category": "transitive verb",
      "definition": "finish, close, end, turn off"
    }
  ],

  "pipi" : [
    {
      "category": "noun",
      "definition": "bug, insect, spider"
    }
  ],

  "poka" : [
    {
      "category": "noun",
      "definition": "side, hip, next to"
    },
    {
      "category": "prep",
      "definition": "in the accompaniment of, with"
    },
    {
      "category": "modifier",
      "definition": "neighbouring"
    }
  ],

  "poki" : [
    {
      "category": "noun",
      "definition": "container, box, bowl, cup, glass"
    }
  ],

  "pona" : [
    {
      "category": "noun",
      "definition": "good, simplicity, positivity"
    },
    {
      "category": "modifier",
      "definition": "good, simple, positive, nice, correct, right"
    },
    {
      "category": "interjection",
      "definition": "great! good! thanks! OK! cool! yay!"
    },
    {
      "category": "transitive verb",
      "definition": "improve, fix, repair, make good"
    },
    {
      "category": "describer",
      "definition": "beneficial; good"
    },
    {
      "category": "describer",
      "definition": "benevolent; altruistic, kind, symbiotic"
    },
    {
      "category": "describer",
      "definition": "helpful; cooperating"
    },
    {
      "category": "describer",
      "definition": "ideal"
    },
    {
      "category": "describer",
      "definition": "conducive to overall wellness"
    }
  ],

  "sama" : [
    {
      "alphaBreak": "true",
      "category": "modifier",
      "definition": "same, similar, equal, of equal status or position"
    },
    {
      "category": "prep",
      "definition": "like, as, seem"
    },
    {
      "category": "adjective",
      "definition": "filling the same or a similar role; equivalent"
    },
    {
      "category": "adjective",
      "definition": "self-"
    }
  ],

  "seli" : [
    {
      "category": "noun",
      "definition": "fire, warmth, heat"
    },
    {
      "category": "modifier",
      "definition": "hot, warm, cooked"
    },
    {
      "category": "transitive verb",
      "definition": "heat, warm up, cook"
    },
    {
      "category": "noun",
      "definition": "fire, a force of nature, destructive chemical reaction"
    },
    {
      "category": "noun",
      "definition": "heat source"
    },
    {
      "category": "noun",
      "definition": "cooking source"
    },
    {
      "category": "noun",
      "definition": "light source"
    },
    {
      "category": "transitive verb",
      "definition": "to use seli on"
    }
  ],

  "selo" : [
    {
      "category": "noun",
      "definition": "outside, surface, skin, shell, bark, shape, peel"
    }
  ],

  "seme" : [
    {
      "category": "other",
      "definition": "what, which, wh- (question word)"
    }
  ],

  "sewi" : [
    {
      "category": "noun",
      "definition": "high, up, above, top, over, on"
    },
    {
      "category": "modifier",
      "definition": "superior, elevated, religious, formal"
    }
  ],

  "sijelo" : [
    {
      "category": "noun",
      "definition": "body, physical state"
    }
  ],

  "sike" : [
    {
      "category": "noun",
      "definition": "circle, wheel, sphere, ball, cycle"
    },
    {
      "category": "modifier",
      "definition": "round, cyclical"
    }
  ],

  "sin" : [
    {
      "category": "modifier",
      "definition": "new, fresh, another, more"
    },
    {
      "category": "transitive verb",
      "definition": "renew, renovate, freshen"
    }
  ],

  "sina" : [
    {
      "category": "noun",
      "definition": "you"
    },
    {
      "category": "modifier",
      "definition": "your"
    }
  ],

  "sinpin" : [
    {
      "category": "noun",
      "definition": "front, chest, torso, face, wall"
    }
  ],

  "sitelen" : [
    {
      "category": "noun",
      "definition": "picture, image"
    },
    {
      "category": "transitive verb",
      "definition": "draw, write"
    },
    {
      "category": "noun",
      "definition": "representation, model"
    },
    {
      "category": "noun",
      "definition": "drawing, print, painting, image, sign, sketch, outline, blueprint, etching, picture"
    },
    {
      "category": "noun",
      "definition": "diagram, chart, graph"
    },
    {
      "category": "noun",
      "definition": "carving, sculpture, figurine, replica"
    }
  ],

  "sona" : [
    {
      "category": "noun",
      "definition": "knowledge, wisdom, intelligence, understanding"
    },
    {
      "category": "transitive verb",
      "definition": "to know, understand, know how to"
    },
    {
      "category": "intransitive verb",
      "definition": "know, understand"
    },
    {
      "category": "kama",
      "definition": "learn, study"
    }
  ],

  "soweli" : [
    {
      "category": "noun",
      "definition": "animal, especially land mammal, lovable animal"
    }
  ],

  "suli" : [
    {
      "category": "modifier",
      "definition": "big, tall, long, adult, important"
    },
    {
      "category": "transitive verb",
      "definition": "enlarge, lengthen"
    },
    {
      "category": "noun",
      "definition": "size"
    }
  ],

  "suno" : [
    {
      "category": "noun",
      "definition": "light"
    }
  ],

  "supa" : [
    {
      "category": "noun",
      "definition": "horizontal surface, e.g furniture, table, chair, pillow, floor"
    }
  ],

  "suwi" : [
    {
      "category": "noun",
      "definition": "candy, sweet food"
    },
    {
      "category": "modifier",
      "definition": "sweet, cute"
    },
    {
      "category": "transitive verb",
      "definition": "sweeten"
    }
  ],

  "tan" : [
    {
      "alphaBreak": "true",
      "category": "prep",
      "definition": "from, by, because of, since"
    },
    {
      "category": "noun",
      "definition": "origin, cause"
    }
  ],

  "taso" : [
    {
      "category": "modifier",
      "definition": "only, sole"
    },
    {
      "category": "conjunction",
      "definition": "but"
    }
  ],

  "tawa" : [
    {
      "category": "prep",
      "definition": "to, in order to, towards, for, until"
    },
    {
      "category": "intransitive verb",
      "definition": "to go to, walk, travel, move, leave"
    },
    {
      "category": "noun",
      "definition": "movement, transportation"
    },
    {
      "category": "modifier",
      "definition": "moving, mobile"
    },
    {
      "category": "transitive verb",
      "definition": "move, displace"
    }
  ],

  "telo" : [
    {
      "category": "noun",
      "definition": "water, liquid, juice, sauce, beverage"
    },
    {
      "category": "transitive verb",
      "definition": "water, wash with water"
    }
  ],

  "tenpo" : [
    {
      "category": "noun",
      "definition": "time, period of time, moment, duration, situation"
    }
  ],

  "toki" : [
    {
      "category": "noun",
      "definition": "language, talking, speech, communication"
    },
    {
      "category": "modifier",
      "definition": "talking, verbal"
    },
    {
      "category": "transitive verb",
      "definition": "to say"
    },
    {
      "category": "intransitive verb",
      "definition": "talk, chat, communicate"
    },
    {
      "category": "interjection",
      "definition": "hello! hi!"
    }
  ],

  "tomo" : [
    {
      "category": "noun",
      "definition": "indoor constructed space, e.g. house, home, room, building"
    },
    {
      "category": "modifier",
      "definition": "urban, domestic, household"
    }
  ],

  "tu" : [
    {
      "category": "modifier",
      "definition": "two"
    },
    {
      "category": "noun",
      "definition": "duo, pair"
    },
    {
      "category": "transitive verb",
      "definition": "double, separate/cut/divide in two"
    }
  ],

  "unpa" : [
    {
      "alphaBreak": "true",
      "category": "noun",
      "definition": "sex, sexuality"
    },
    {
      "category": "modifier",
      "definition": "erotic, sexual"
    },
    {
      "category": "transitive verb",
      "definition": "to have sex with"
    },
    {
      "category": "intransitive verb",
      "definition": "have sex"
    }
  ],

  "uta" : [
    {
      "category": "noun",
      "definition": "mouth"
    },
    {
      "category": "modifier",
      "definition": "oral"
    }
  ],

  "utala" : [
    {
      "category": "noun",
      "definition": "conflict, disharmony, competition, fight, war, battle, attack, blow, argument"
    },
    {
      "category": "transitive verb",
      "definition": "hit, strike, attack, compete against"
    }
  ],

  "walo" : [
    {
      "alphaBreak": "true",
      "category": "modifier",
      "definition": "white, light (colour)"
    },
    {
      "category": "noun",
      "definition": "white thing or part, whiteness, lightness"
    }
  ],

  "wan" : [
    {
      "category": "modifier",
      "definition": "one, a"
    },
    {
      "category": "noun",
      "definition": "unit, element, particle, part, piece"
    },
    {
      "category": "transitive verb",
      "definition": "unite, make one"
    }
  ],

  "waso" : [
    {
      "category": "noun",
      "definition": "bird, winged animal"
    }
  ],

  "wawa" : [
    {
      "category": "noun",
      "definition": "energy, strength, power"
    },
    {
      "category": "modifier",
      "definition": "energetic, strong, fierce, intense, sure, confident"
    },
    {
      "category": "transitive verb",
      "definition": "strengthen, energize, empower"
    }
  ],

  "weka" : [
    {
      "category": "modifier",
      "definition": "away, absent, missing"
    },
    {
      "category": "noun",
      "definition": "absence"
    },
    {
      "category": "transitive verb",
      "definition": "throw away, remove, get rid of"
    }
  ],

  "wile" : [
    {
      "category": "transitive verb",
      "definition": "to want, need, wish, have to, must, will, should"
    },
    {
      "category": "noun",
      "definition": "desire, need, will"
    },
    {
      "category": "modifier",
      "definition": "necessary"
    }
  ]

}

def lambda_handler(event, context):
    if (event['session']['application']['applicationId']
 != APPLICATION):
        raise ValueError("Unauthorized application.")

    request_type = event['request']['type']
    if (request_type == "LaunchRequest"):
        return on_launch(event, context)
    elif (request_type == "IntentRequest"):
        return on_intent(event, context)

def on_intent(event, context):
    if (event['request']['intent']['name'] == "GetWordIntent"):
        build_response({},build_speechlet_response("Toki Pona Words", get_random_word(), "", True))

def on_launch(event, context):
    return get_welcome_response()

def get_welcome_response:
    return build_response({}, build_speechlet_response("Toki Pona Words",
        "This is the Toki Pona Words skill." +
        "I will give you a random Toki Pona word out of the entirety of the language and then I will give you its definition."
        "Ask me to give you a random Toki Pona word.", False))

def get_random_word:
    word = random.choice(VOCAB.keys())
    slot = random.choice(VOCAB[word])
    category = slot['category']
    definition = slot['definition']
    return "{} is a {} in Toki Pona which means {}.".format(word,category,definition)
            
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }
            
def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }

