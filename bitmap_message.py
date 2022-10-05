bitmap = """
14. ....................................................................
15.    **************   *  *** **  *      ******************************
16.   ********************* ** ** *  * ****************************** *
17.  **      *****************       ******************************
18.           *************          **  * **** ** ************** *
19.            *********            *******   **************** * *
20.             ********           ***************************  *
21.    *        * **** ***         *************** ******  ** *
22.                ****  *         ***************   *** ***  *
23.                  ******         *************    **   **  *
24.                  ********        *************    *  ** ***
25.                    ********         ********          * *** ****
26.                    *********         ******  *        **** ** * **
27.                    *********         ****** * *           *** *   *
28.                      ******          ***** **             *****   *
29.                      *****            **** *            ********
30.                     *****             ****              *********
31.                     ****              **                 *******   *
32.                     ***                                       *    *
33.                     **     *                    *
34. ...................................................................."""

message = """L Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean
commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis
dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies
nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.
Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.
In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam
dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.""".split("\n")

for x in message:
    for y in x:
        if y == " ":
            continue
        bitmap = bitmap.replace("*", y, 1)

print(bitmap)    
      