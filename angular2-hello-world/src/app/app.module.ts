import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { PrimeiroComponent } from './primeiro/primeiro.component';
import { CursosComponent } from './cursos/cursos.component';


@NgModule({
  declarations: [
    AppComponent, 
    PrimeiroComponent, 
    CursosComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
