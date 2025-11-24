def show_intro():
    print("I love animals!")
    print("Let's check out the animals...")
    print("The deer looks fine.")
    print("The lion looks healthy.")

def get_ascii_animals():
    camel = r"""
The camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
"""

    lion = r"""
The lion habitat...
                                                     ,w.
                                                   ,YWMMw  ,M  ,
                           _.----.._   __..-----._.'MMMMMw,wMWmW,
                      _.-""         '''             YP"WMMMMMMMMMb,
                   .-' __.'                       .'    MMMMW^WMMMM;
        _,       .'.-'"; `,          /`      .--""     :MMM[==MWMW^;
     ,mM^"     ,-'.'  /    ;        ;       /  ,       MMMMb_wMW"  @\
    ,MM:.    .'.-'  .'      ;       `\     ;   `,      MMMMMMMW `"=./`-,
    WMMm__,-'.'    /       _.\         F'''-+,, ;_,_.dMMMMMMMM[,_ / `=_}
    "^MP__.-'   ,-'  _.--""   `-,     ;      \  ; ;MMMMMMMMMMW^``; __|
               /   .'            ;   ;        )  )`{  \ `"^W^`,   \  :
              /  .'             /   (       .'  /     Ww._     `.  `"
             /  Y,              `,   `-,=,_{   ;      MMMP`""-,  `-._.-,
            (--, )                `,_ / `)  \/"")      ^"      `-, -;"\:
"""

    deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
"""

    goose = r"""
The goose habitat...

                                       _
                                   ,-"" "".
                                 ,'   ____ `.
                               ,'   ,'    `. `._
      (`.         _..--.._   ,'   ,'        \   \
     (`-.\    .-""        ""'    /          ( d _b
    (`._  `-"" ,._              (            `-( \
    <_ `      ( <`<              \            `-._\
     <`-       (__< <             :
      (__       (_<_<             ;
       `------------------------------------------
"""

    bat = r"""
The bat habitat...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
"""

    rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y    
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
"""

    return [camel, lion, deer, goose, bat, rabbit]

def show_habitat(animals, index):
    print(animals[index])

def zoo_loop():
    animals = get_ascii_animals()
    while True:
        user_input = input("Please enter the number of the habitat you would like to view (or 'exit' to quit):\n>>> ")
        if user_input == "exit":
            print("See you later!")
            break
        elif user_input.isdigit():
            index = int(user_input)
            if 0 <= index < len(animals):
                show_habitat(animals, index)
            else:
                print("Invalid number, try again.")
        else:
            print("Invalid input.")

def main():
    show_intro()
    zoo_loop()

main()
