import unittest
import basico.basico as c

class testeoBasicos(unittest.TestCase):

    def test_es_par(self):
        self.assertTrue(c.es_par(0))
        self.assertTrue(c.es_par(2))
        self.assertFalse(c.es_par(3))
        self.assertFalse(c.es_par(8645))
        self.assertTrue(c.es_par(3572))

    def test_dos_pertenece(self):
        self.assertTrue(c.dos_pertenece([1,2,3,4]))
        self.assertFalse(c.dos_pertenece([1,3,4,5,6,12]))
        self.assertTrue(c.dos_pertenece([0,0,0,0,0,0,0,0,0,2]))
        self.assertFalse(c.dos_pertenece([0,0,0,0]))
        self.assertTrue(c.dos_pertenece([3,6,4,5,7,5,7,8,5,1,2,5,3,6,7,5,4556,2]))
        self.assertTrue(c.dos_pertenece([1,1,1,2,2,2,2,3,3,3,]))
        self.assertTrue(c.dos_pertenece([2,2,2,2,2,2,2]))
        self.assertTrue(c.dos_pertenece([2]))
        self.assertTrue(c.dos_pertenece([2,3,4,5]))
        self.assertFalse(c.dos_pertenece([3]))
        self.assertFalse(c.dos_pertenece([]))
                        
    def test_pertenece(self):
        self.assertFalse(c.pertenece([1,2,3,4],5))
        self.assertFalse(c.pertenece([1,2,3,4,5,6,7],0))
        self.assertFalse(c.pertenece([3],2))
        self.assertFalse(c.pertenece([],3))
        self.assertTrue(c.pertenece([1,2,3,4],3))
        self.assertTrue(c.pertenece([1,1,1,1,1],1))
        self.assertTrue(c.pertenece([1,2,3,4,5,6,7,8,9,10],10))
        self.assertTrue(c.pertenece([2],2))

    def test_mas_larga(self):
        self.assertEqual([1,2,3],c.mas_larga([1,2,3],[1,2]))
        self.assertEqual([1,2,3,4,5],c.mas_larga([1,2,3],[1,2,3,4,5]))
        self.assertEqual([1],c.mas_larga([1],[]))
        self.assertEqual([1,2,3],c.mas_larga([1,2,3],[1,2,3]))
        self.assertEqual([1,2,3,4,5,6,7],c.mas_larga([1,2,3,4,5,6,7],[1,2]))
        self.assertEqual([],c.mas_larga([],[]))

    def test_cant_e(self):
        self.assertEqual(1,c.cant_e(['a','e','i','o','u']))
        self.assertEqual(2,c.cant_e(['a','e','i','o','e']))
        self.assertEqual(4,c.cant_e(['a','e','e','e','e']))
        self.assertEqual(0,c.cant_e(['a','i','o','u','d','r']))
        self.assertEqual(1,c.cant_e(['a','i','o','u','a','i','o','u','d','r','e']))
        self.assertEqual(5,c.cant_e(['e','e','e','e','e']))
    
    def test_sumar_unos(self):
        self.assertEqual([2,3,4,5],c.sumar_unos([1,2,3,4]))
        self.assertEqual([5,4,3,2,1],c.sumar_unos([4,3,2,1,0]))
        self.assertEqual([-2,-1,0,1,2],c.sumar_unos([-3,-2,-1,0,1]))
        self.assertEqual([10],c.sumar_unos([9]))
        self.assertEqual([],c.sumar_unos([]))


    def test_mezclar(self):
        self.assertEqual("PJeopsee",c.mezclar("Pepe","Jose"))
        self.assertEqual("PJeopseefa",c.mezclar("Pepe","Josefa"))
        self.assertEqual("tumpa",c.mezclar("tma","up"))
        self.assertEqual("bumbap",c.mezclar("bma","ubp"))
        self.assertEqual("JAJAJAJAJAJAA",c.mezclar("JJJJJJ","AAAAAAA"))
    