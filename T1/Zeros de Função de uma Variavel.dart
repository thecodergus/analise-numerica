typedef F = double Function(double);
class Pair<T1, T2> {
    Pair(this.a, this.b);
    T1 a;
    T2 b;

    T1 first() => this.a;
    T2 second() => this.b;
}

class T1Zeros{
    T1Zeros(this._f);
    F _f;

    double _df(double x, {double h = 0.00000000001}) => (this._f(x + h) - this._f(x)) / h;

    double bissecao(Pair<double, double> intervalo, {int interacoes = 100}){
        double a = intervalo.first();
        double b = intervalo.second();
        double aprox = 0;


        for(int i = 0; i < interacoes; i++){
            aprox = (a + b) / 2;

            if(this._f(b) * this._f(aprox) < 0) a = aprox;
            if(this._f(a) * this._f(aprox) < 0) b = aprox;
        }

        return aprox;
    }

    double newton(double x0, {int interacoes = 100}){
        for(int i = 0; i < interacoes; i++) x0 -= this._f(x0) / this._df(x0);

        return x0;
    }

    double posicao_falsa(Pair<double, double> intervalo, {int interacoes = 100}){
        double a = intervalo.first();
        double b = intervalo.second();
        double c = 0;

        for(int i = 0; i < interacoes; i++){
            double fa = this._f(a);
            double fb = this._f(b);

            c = (a * fb - b * fa) / (fb - fa);

            if(c == 0){
                break;
            }else if(this._f(c) * fa < 0){
                b = c;
            }else{
                a = c;
            }
        }

        return c;
    }

    double secate(Pair<double, double> intervalo, {int interacoes = 100}){
        double x0 = intervalo.first();
        double x1 = intervalo.second();
        double x2 = 0;

        for(int i = 0; i < interacoes; i++){
            double fx0 = this._f(x0);
            double fx1 = this._f(x1);

            x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
            double c = fx0 * fx1;

            x0 = x1;
            x1 = x2;

            if(c == 0) return x2;
        }

        return x2;
    }

}

void main(){
    print("Ola Mundo");
}