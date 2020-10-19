from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np 
 
sample_size = 1000
RANGE = [[2, 8], [5, 11]]
BINS = 10
 
 
 
def cholesky(sigma):
    var11 = sigma[0][0]
    var22 = sigma[1][1]
    cov = sigma[0][1]
    std1 = np.sqrt(var11)
    std2 = np.sqrt(var22)
    rho = cov/(std1*std2)
    
    A = np.array([
        [std1, 0],
        [rho*std2,  np.sqrt(1-rho**2)*std2]
    ])
    
    return A
 
 
for a in [-0.5, 0., 0.5, 1]:
    mu = np.array([[5],
                   [8]])
    sigma = np.array([[1,   2*a],
                      [2*a, 4  ]])
    if a==1 :
        A = np.array([[1., 0.],
                      [2., 0.]])
    else :
        A = cholesky(sigma)        
 
    normal_sample = np.random.normal(size=(2, sample_size))
    X = np.dot(A, normal_sample) + mu


    hist2d, xedges, yedges = np.histogram2d(X[0], X[1], bins=BINS, range=RANGE)


    xpos, ypos = np.meshgrid(
        (xedges[:-1]+xedges[1:])/2 ,
        (yedges[:-1]+yedges[1:])/2 ,
        indexing="ij")


    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
    ax.plot_surface(xpos, ypos, hist2d, cmap='magma')
    ax.set_title(f'Distribution, a={a}')
    ax.set_xlabel('$X_{1}$')
    ax.set_ylabel('$X_{2}$')
    ax.set_zlabel('freq')
    fig.savefig(f'distribution_3d_{a}.png')
    plt.show()

    if(a!=1):
        # marginal density
        x1 = X[0, :]
        hist0, bin_edges = np.histogram(x1, range=RANGE[0], bins=2*BINS, density=True)
        plt.plot((bin_edges[1:]+bin_edges[:-1])/2, hist0)
        plt.title(f'Simulated marginal density $X_1$ (a={a})')
        plt.savefig(f'simulated_marg_x1_{a}.png')
        plt.show()
        
        x2 = X[1, :]
        hist1, bin_edges = np.histogram(x2, range=RANGE[1], bins=2*BINS, density=True)
        plt.plot((bin_edges[1:]+bin_edges[:-1])/2, hist1)
        plt.title(f'Simulated marginal density $X_2$ (a={a})')
        plt.savefig(f'simulated_marg_x2_{a}.png')
        plt.show()

        #joint_density
        hist2d, xedges, yedges = np.histogram2d(X[0], X[1], bins=BINS, range=RANGE,density='true')

        xpos, ypos = np.meshgrid(
        (xedges[:-1]+xedges[1:])/2 ,
        (yedges[:-1]+yedges[1:])/2 ,
        indexing="ij")

        fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
        ax.plot_surface(xpos, ypos, hist2d, cmap='magma')
        ax.set_title(f'Simulated Joint density, a={a}')
        ax.set_xlabel('$X_{1}$')
        ax.set_ylabel('$X_{2}$')
        fig.savefig(f'simulated_3d_{a}.png')
        plt.show()


        
        sigma_inv = np.linalg.inv(sigma) #sigma inverse
        sqrt_det = np.linalg.det(sigma)**0.5
        
        
        xedges = np.linspace(RANGE[0][0], RANGE[0][1], BINS+1)
        yedges = np.linspace(RANGE[1][0], RANGE[1][1], BINS+1)
        xs, ys = np.meshgrid(
            (xedges[:-1]+xedges[1:])/2 ,
            (yedges[:-1]+yedges[1:])/2 ,
            indexing="ij")

        xs_mean = xs - mu[0]
        ys_mean = ys - mu[1]
        zs = np.exp(-0.5*(sigma_inv[0,0]*xs_mean**2 + (sigma_inv[0,1]+sigma_inv[1,0])*xs_mean*ys_mean + sigma_inv[1,1]*ys_mean**2))/(2*np.pi*sqrt_det)
        zs = zs*(sample_size/2)
        
        # show joint density
        fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
        ax.plot_surface(xs, ys, zs, cmap='magma')
        ax.set_title(f'Actual_3d_distribution a={a}')
        ax.set_xlabel('$X_{1}$')
        ax.set_ylabel('$X_{2}$')
        ax.set_zlabel('freq')
        fig.savefig(f'actual_3d_distribution_{a}.png')
        plt.show()

        # marginal density
        x1 = np.linspace(RANGE[0][0], RANGE[0][1], BINS*8)
        plt.plot(x1, np.exp(-((x1-mu[0,0])**2)/sigma[0,0])/np.sqrt(2*np.pi*sigma[0,0]))
        plt.title(f'Actual marginal density $X_1$ (a = {a})')
        plt.savefig(f'actual_marg_x1_{a}.png')
        plt.show()

        x2 = np.linspace(RANGE[1][0], RANGE[1][1], BINS*8)
        plt.plot(x2, np.exp(-((x2-mu[1,0])**2)/sigma[1,1])/np.sqrt(2*np.pi*sigma[1,1]))
        plt.title(f'Actual marginal density $X_2$ (a = {a})')
        plt.savefig(f'actual_marg_x2_{a}.png')
        plt.show()
        plt.clf()