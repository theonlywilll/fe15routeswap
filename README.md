# Fire Emblem Echoes: Route Swap Patch

This is a patch that swaps units on Alm's and Celica's route of the game. So instead of controlling Alm in act 1, you will control Celica instead.

Credits to KrashBoomBang for calculating all the unit stats, and balance changes. And a big thanks to the 3DSFE ROM Hacking for helping with a lot of stuff.

Due to limitations, some gameplay changes had to be made: (Other than the units)

- Celica (Alm's replacement) will be force promoted after talking to the sage in Sage's Hamlet, instead of allowing the class to promote in Mila's shrines.

- All ranked supports are now passives with their C rank bonuses. Support conversations can still happen but they change nothing gameplay wise.

- The location of Valbar's Squad in Barth's map is changed since their replacements are extremely frail and could easily die before even the player could help them.

- NPC Clive (now replacing Palla) has been moved a bit foward so he doesn't get stuck in a mountain.

### Notes

- Weapons locks has not been changed internal-unit wise, meaning Celica (Alm's replacement) can use the Royal Sword and the Falchion, while Alm (Celica's replacement) can use the Beloved Zofia.

- Passive supports, spell lists for characters aren't touched. (Of course with the exception of ranked supports, as said above)

## Install instructions

### 1. Get the game files

You will need to get the game files from your copy to patch them. See here:

https://gbatemp.net/threads/tutorial-how-to-decrypt-extract-rebuild-3ds-cia-cxi-files.383055/

Note: Only v9 of HackingToolkit3DS can extract FE15 files:

https://github.com/Asia81/HackingToolkit9DS-Deprecated-/releases/tag/9

### 2. Find the folder with the Data

After extracting the game files, search for a folder named "ExtractedRomFS". Inside it, will be a folder named Data. Copy it, paste it somewhere.

### 2. Patching the files

Now, you can choose if you want to patch the files manually or use the automatic patcher. It is extremely recommended to use the automatic patcher provided, but both options are available.

#### 2.1 Automatic patch

1. Download the patch program.

2. Grab your Data folder from before, place it in the same place as the patch program.

3. Rename it "vanilla" (with the exact lowercase name)

4. Open the patcher, then hit "Patch!" and wait for it do be finished.

5.1 If a error text appeared, revise the steps again.

6. Done! It now will be a folder called "patched", these contain the patched files.

#### 2.2 Manual patch

1. Download the patch program, it will be a folder called "routeswap".

2. Get a IPS patcher, then manually patch every file from Data with the same name as the .IPS file (ex: Person.bin.lz.ips will patch Person.bin.lz).

3. Done. Make sure to have the patched files in a separate folder.

### 3. Installing it

It exists two methods to use it: Repack it again, and use Luma3DS to patch your game.

If you want to repack it to use with Citra, follow the instructions on the link mentioned above:

https://gbatemp.net/threads/tutorial-how-to-decrypt-extract-rebuild-3ds-cia-cxi-files.383055/

If you want to use luma3DS (the easier way):

1. Grab your folder with the patched files.

1.1. Rename it "Data" if it is not named that way.

2. You will need to have luma3DS installed in your 3DS.

3. In your SDcard, go to the folders luma/titles.

4. If it does not exist, create a folder with the echoes title ID.

Title IDs for each version of Echoes:

US: 00040000001B4000

EUR: 00040000001B4100

JPN: 00040000001A2B00

5. Now, create a folder named "romfs" inside of it.

6. Paste the "Data" folder in it.

7. Make sure the luma3DS patching is enabled.

7.1 To enable it, see this link: https://github.com/AuroraWright/Luma3DS/wiki/Optional-features

8. Done!

Hope you have fun with it!