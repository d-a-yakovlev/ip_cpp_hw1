#include "string_holder/string_holder.hpp"

//#define INTEGRATE // macros for reduce text in "user console interface"


void callContextMenu(); // init context menu cycle
void lexSort(StringHolder& h); // lexicographic sort Zac3A2 -> 23AZac


int main()
{
    callContextMenu();

    return 0;
}


void callContextMenu()
{
    bool isActual = true;
    while (isActual)
    {
#ifndef INTEGRATE
        std::cout << "Choose prefered string type to StringHolder :\n"
            << "std::string[1] or std::string_view[2]" << std::endl;
#endif

        char inputKey = '\0';
        bool isCorrectInput = false;
        while ( !isCorrectInput )
        {
            std::cin >> inputKey;
            if ( inputKey == '1' || inputKey == '2' ) isCorrectInput = true;
            else 
            {
                std::cout << "Please try again..." << std::endl;
                isCorrectInput = false;
            }
        }
#ifndef INTEGRATE
        std::cout << "Write text what you want place in StringHolder :" << std::endl;
#endif
        std::string sdata;
        StringHolder holder;
#ifdef INTEGRATE
        std::cin >> sdata;
#else
        std::cin.ignore();
        std::getline(std::cin, sdata);
#endif
        std::cout << "Your input : "<< sdata << " {" << sdata.size() << "}" << std::endl;
        switch(inputKey)
        {
            case '1':
                holder = StringHolder(sdata);
                break;
            case '2':
                holder = StringHolder(std::string_view(sdata));
                break;
        }

        std::cout << "Data in holder : [" << holder << "] {" << holder.size() << "}" << std::endl;
#ifndef INTEGRATE
        std::cout << "\n+==========================================+\n"
            << "|Let's try our StringHolder with your data |\n"
            << "|try lexicographic sort data in Holder     |\n"
            << "|this should check Holder behavior         |\n" 
            << "+==========================================+\n" << std::endl;
#endif
        
        lexSort(holder);

        std::cout << "Data in holder after sort : [" << holder << "]" << std::endl;
#ifndef INTEGRATE
        std::cout << "\nHolder nice working as some sort of container!"
            << "\n\nWould you try another data for this pipeline?"
            << "\n Yes[y] or No[n]"
            << std::endl;
#endif

        isCorrectInput = false;
        while ( !isCorrectInput )
        {
            std::cin >> inputKey;
            if ( inputKey == 'y' || inputKey == 'n' ) isCorrectInput = true;
            else 
            {
                std::cout << "Please try again..." << std::endl;
                isCorrectInput = false;
            }
        }

        if (inputKey == 'n') isActual = false;
    }

    std::cout << "Bye." << std::endl;
}


void lexSort(StringHolder& holder)
{
    static std::string content;
    content = holder.string();
    std::sort( content.begin(), content.end() );
    
    holder.update(std::string_view(content));
}