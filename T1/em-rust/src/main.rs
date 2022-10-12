type Intervalo = (f64, f64);

#[derive(Debug)]
struct T1Zeros{
	_f: calculi::Equation
}


impl T1Zeros{

    fn new(_f: fn(f64) -> f64) -> Self{
        T1Zeros{
            _f
        }
    }

    fn f(&self, x: f64) -> f64{
        (self._f)(x)
    }

    fn df(&self, x: f64) -> f64{
        // let h: &f64 = &std::f64::MIN_POSITIVE;
        let h: f64 = std::f64::MIN_POSITIVE;

        return (self.f(x + h) - self.f(x)) / h;
    }

    fn bissecao(&self, intervalo: &Intervalo, interacoes: &u64) -> f64{
        let (mut a, mut b): (f64, f64) = *intervalo;
        let mut aprox: f64 = 0_f64; 

        for _ in 0..*interacoes{
            aprox = (a + b) / 2_f64;

            if self.f(b) * self.f(aprox) < 0_f64{
                a = aprox;
            }else if self.f(a) * self.f(aprox) < 0_f64{
                b = aprox;
            }
        }

        return aprox;
    }

    fn newton(&self, x0: &mut f64, interacoes: u64) -> f64{
        match interacoes{
            0 => 0_f64,
            n => self.f(*x0) / self.df(*x0) - self.newton(x0, n - 1)
        }
    }

    fn posicao_falsa(&self, intervalo: &mut Intervalo, interacoes: &u64) -> f64{
        let (a, b): &mut Intervalo = intervalo;
        let mut c: f64 = 0_f64;

        for _ in 0..*interacoes{
            let (fa, fb): (f64, f64) = (self.f(*a), self.f(*b));

            if c == 0_f64 {
                return c;
            }else if self.f(c) * fa < 0_f64 {
                *b = c;
            }else{
                *a = c;
            }
        }

        return c;
    }

    fn secante(&self, intervalo: &mut Intervalo, interacoes: &u64) -> f64{
        let (x0, x1): &mut Intervalo = intervalo;
        let mut x2: f64 = 0_f64;

        for _ in 0..*interacoes{
            let (fx0, fx1): (f64, f64) = (self.f(*x0), self.f(*x1));
            
            x2 = (*x0 * fx1 - *x1 * fx0) / (fx1 - fx0);

            if fx0 * fx1 == 0_f64 {
                return x2
            }

            (*x0, *x1) = (*x1, x2);
        }

        return x2;
    }
}

fn main() {

    // https://docs.rs/calculi/latest/calculi/#structs
    // let f = calculi::Equation::new("");

    let f: fn(f64) -> f64 = |c: f64| -> f64{
        let (g, m, v, t, e): (f64, f64, f64, f64, &f64) = (
            9.81,
            71.59,
            51.63,
            9.5,
            &std::f64::consts::E
        );

        return ((g * m) / c) * (1_f64 - (*e).powf(-(c / m)*t)) - v;
    };

    let t: T1Zeros = T1Zeros::new(f);

    // Bissecao
    let mut inter1: Intervalo = (0.27, 57.62);
    for mut i in vec![2,4,12]{
        println!("{:.11},", t.bissecao(&mut inter1, &mut i));
    }


    // Newton
    let mut inter2: f64 = 1.21;
    for mut i in vec![1,3,5]{
        println!("{:.11},", t.newton(&mut inter2, i));
    }
}
