#include "funciones.h"

void enviaruart1(int sl){
char rec1[20] ;
	sprintf(rec1,"%d",readTemp(sl));
	serial_print_str(rec1);
	serial_println_str(" C       ");
	_delay_ms(100);
	if (readTemp(sl) <=0) {
	       serial_println_str(" helado"); }
	    else if ((readTemp(sl)>0)  & (readTemp(sl)<=20)) {
	       serial_println_str("frío");  }
	    else if ((readTemp(sl)>20)  & (readTemp(sl)<=30)) {
	       serial_println_str("normal");  }
	    else if ((readTemp(sl)>30)  & (readTemp(sl)<=40)) {
	       serial_println_str("calentando");  }
	       else {
	       serial_println_str("alerta");  }
}
/*
void enviaruart2(){
char rec2[10] ;
	sprintf(rec2,"%d",readTemp(2));
	 serial_print_str(rec2);
	 serial_println_str(" C");
	_delay_ms(100);
}
*/
